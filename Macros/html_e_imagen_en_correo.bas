Attribute VB_Name = "Módulo1"
Sub Enviar_Email()
    'Declaraciones de variables
    
    'Variables para crear el correo de Outlook
    Dim OutlookApp As Outlook.Application
    Dim MItem As MailItem
    
    Dim ruta As String
    Dim carpeta As String
    Dim archivo As String
    
    'Variables para crear el contenido del correo
    Dim Correo As String
    Dim Destinatario As String
    Dim Hora As String
    Dim Sala As String
    Dim msg As String
    Dim rango As String
    
    
    ruta = "C:\Users\Joseph\Desktop"
    carpeta = "\imagenes_enviadas"
    'Asunto, el mismo para todos los correos
    Asunto = Worksheets("Lista").Range("B1").Value
    rango = Worksheets("Lista").Range("B2").Value
    
    'Bucle, la variable CeldaCorreo variar? en cada celda del rango
    For Each CeldaCorreo In Worksheets("Lista").Range(rango)
      
            
        'Asignacion de valor a las variables,
        'con respecto a la variable CeldaCorreo
           
        Correo = CeldaCorreo.Value
        Destinatario = CeldaCorreo.Offset(0, -1).Value
          
        ' Exportar imagen
        Call ExportarImagen(ruta, carpeta, Destinatario)
        'Crear el mensaje con las variables
            
        msg = "Estimado(a) " & Destinatario & ",<br><br>"
        msg = msg & "<br>La presente es para recordarle<br>"
        
        'Crear correo de Outlook
        Set OutlookApp = CreateObject("Outlook.Application")
        Set MItem = OutlookApp.CreateItem(olMailItem)
        
        'Asignar el contenido al correo
        With MItem
            .To = Correo
            .Subject = Asunto
            archivo = Destinatario & ".jpg"
            .Attachments.Add ruta & carpeta & "\" & archivo
            .BodyFormat = olFormatHTML
            '.Body = msg
            .HTMLBody = _
                "<HTML> " & _
                    "<BODY>" & _
                        msg & _
                        "<img src=cid:" & archivo & " height=150 width=275>" & _
                    "</BODY> " & _
                "</HTML>"
            .Send
        End With
        
        'Limpiar las variables del correo
        Set OutlookApp = Nothing
        Set MItem = Nothing
    Next CeldaCorreo
    'Lo siguiente imprime el contenido de la macro
    'MsgBox Msg
End Sub

Function Desagrupar(name As String, sheet As String) As Boolean
    Dim grupo As Shape
    Desagrupar = False
    For Each grupo In Worksheets(sheet).Shapes
        If grupo.name = name Then
            grupo.Ungroup
            Desagrupar = True
            Exit For
        End If
    Next grupo
End Function


Sub ExportarImagen(ruta As String, carpeta As String, nombre As String)
    
    
    Dim imagen_exportar As Shape
    Dim texto_forma As Shape
    Dim mensage_forma As String
    
    
    ' Desagrupa la forma "Grupo" en las formas "Fondo" y "Texto"
    If Desagrupar("Grupo", "Imagen") Then
        ' Busca y elimina la forma "Texto"
        For Each texto_forma In Worksheets("Imagen").Shapes
            If texto_forma.name = "Texto" Then
                texto_forma.Delete
                Exit For
            End If
        Next texto_forma
    End If
        
    ' Generar Mensaje
    mensage_forma = "Feliz" & Chr(13) & "Cumpleaños" & Chr(13) & nombre
    
    With Worksheets("Imagen")
        ' Genera la forma "Texto"
        Worksheets("Imagen").Shapes.AddTextEffect(msoTextEffect48, mensage_forma, "+mn-lt", 46, msoTrue, msoFalse, 50, 100).name = "Texto"
        
        ' Agrupa las formas "Fondo" y "Texto" en la forma "Grupo"
        .Shapes.SelectAll
        With .Shapes.Range(Array("Fondo", "Texto"))
            .Group
            .name = "Grupo"
        End With
    End With
    
    Application.ScreenUpdating = False
    For Each imagen_exportar In Worksheets("Imagen").Shapes
        'añadimos un gráfico
        Charts.Add
        'lo situamos como objeto en la Hoja Imagen
        ActiveChart.Location Where:=xlLocationAsObject, name:="Imagen"
        Set chrt = Worksheets("Imagen").ChartObjects(1)
            nombreimg = imagen_exportar.name
            'adaptamos tamaño de imagen y gráfico
            With imagen_exportar
                chrt.Width = .Width
                chrt.Height = .Height
                'copiamos la imagen
                .Copy
            End With
            'pegamos dentro del gráfico la imegen
            ActiveChart.Paste
            'exportamos el gráfico con el nombre del objeto (imagen)
            If Dir(ruta) = "" Then
                'Comprueba que la carpeta no exista para crear el directorio.
                If Dir(ruta & carpeta, vbDirectory + vbHidden) = "" Then
                    MkDir ruta & carpeta
                End If
            End If
            chrt.Chart.Export Filename:=ruta & carpeta & "\" & nombre & ".jpg"
        chrt.Delete
    Next imagen_exportar
    Application.ScreenUpdating = True
End Sub
