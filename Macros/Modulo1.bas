Attribute VB_Name = "Modulo1"
Sub Enviar_Email()

'Declaraciones de variables

    'Variables para crear el correo de Outlook
Dim OutlookApp As Outlook.Application
Dim MItem As MailItem

    'Variables para crear el contenido del correo
Dim Correo As String
Dim Destinatario As String
Dim Hora As String
Dim Sala As String
Dim Msg As String

    'Asunto, el mismo para todos los correos
Asunto = Worksheets("Hoja1").Range("B1").Value

    'Bucle, la variable CeldaCorreo variar� en cada celda del rango
For Each CeldaCorreo In Range("B6:B8")
  
        
    'Asignaci�n de valor a las variables, con respecto a la variable CeldaCorreo
       
    Correo = CeldaCorreo.Value
    Destinatario = CeldaCorreo.Offset(0, -1).Value
    Sala = CeldaCorreo.Offset(0, 2).Value
    Hora = CeldaCorreo.Offset(0, 1).Value
      
        
    'Crear el mensaje con las variables
        
    Msg = "Estimado(a) " & Destinatario & "," & vbNewLine & vbNewLine
    Msg = Msg & "La presente es para recordarle"
    Msg = Msg & "que hoy se llevar� acabo el Programa Nutricional ViveRebien en la " & Sala & "."
    Msg = Msg & " En su caso, la consulta ser� a las " & Hora & vbNewLine & vbNewLine
    Msg = Msg & "Agradeceremos pueda asistir puntualmente," & vbNewLine
    Msg = Msg & "Saludos."
    
    'Crear correo de Outlook
    Set OutlookApp = CreateObject("Outlook.Application")
    Set MItem = OutlookApp.CreateItem(olMailItem)
    
    'Asignar el contenido al correo
    With MItem
        .To = Correo
        .Subject = Asunto
        .Body = Msg
        .Send
    End With
    
    'Limpiar las variables del correo
    Set OutlookApp = Nothing
    Set MItem = Nothing
Next
'Lo siguiente imprime el contenido de la macro
'MsgBox Msg
End Sub

