Attribute VB_Name = "Módulo21"
Sub Filtro()
Attribute Filtro.VB_ProcData.VB_Invoke_Func = " \n14"

' Filtro Macro
' Macro para Empleados
    ' Declaración de variables
    
    Dim textC As String
    Dim NR As String
    
    
    ' ****** Empleados (Emp) ******
    ' Filtrado Avanzado de Empleados desde la tabla general
    ' es decir, recopiar los datos de la tabla general seleccionada y
    ' nombrada como Datos_Generales
    Sheets("GENERAL").Range("Datos_Generales").AdvancedFilter Action:= _
        xlFilterCopy, CriteriaRange:=Range("Fil_Avan_Emp[#All]"), CopyToRange _
        :=Range("Emp_F.Av!A5"), Unique:=False

    ' Formato de Tabla
    ' Según la cantidad de empleados de la UN/Empresa y el proyecto
    ' Paso 1: Conteo de las columnas
    textC = Sheets("GENERAL").Range("Datos_Generales").Address      ' textC = "$A$1:$CA$5373"
    textC = Right(textC, Len(textC) - InStr(textC, ":"))            ' textC = "$CA$5373"
    textC = Right(textC, Len(textC) - InStr(textC, "$"))            ' textC = "CA$5373"
    textC = Left(textC, InStr(textC, "$") - 1)                      ' textC = "CA"
    
    ' Paso 2: Conteo de las filas
    ' Utilizando la columna -> Plantilla
    NR = CStr(Sheets("Emp_F.Av").Cells(Rows.Count, 2).End(xlUp).Row)
    
    ' Paso 3: Agregar el formato a los datos filtrados para Empleados
    ' Según textC y NR calculados en los pasos 1 y 2
    ' que nos dan las dimensiones de la tabla
    Sheets("Emp_F.Av").ListObjects.Add(xlSrcRange, Range("Emp_F.Av!$A$5:$" & textC & "$" & NR), , xlYes).Name = _
        "Tabla_Fil_Avan_Emp"
     
    ' ****** Obreros (Obr) ******
    ' Filtrado Avanzado de Obreros desde la tabla general
    Sheets("GENERAL").Range("Datos_Generales").AdvancedFilter Action:= _
       xlFilterCopy, CriteriaRange:=Range("Fil_Avan_Obr[#All]"), CopyToRange _
       :=Range("Obr_F.Av!A5"), Unique:=False
       
    ' Formato de Tabla
    ' Según la cantidad de empleados de la UN/Empresa y el proyecto
    ' Paso 1: Conteo de las columnas (es el mismo que el de Empleados)
    ' Paso 2: Conteo de las filas (es el mismo que el de Empleados)
    ' Utilizando la columna -> Plantilla
    NR = CStr(Sheets("Obr_F.Av").Cells(Rows.Count, 2).End(xlUp).Row)
    
    ' Paso 3: Agregar el formato a los datos filtrados Para Obreros
    ' Según textC y NR calculados en los pasos 1 y 2
    ' que nos dan las dimensiones de la tabla
    Sheets("Obr_F.Av").ListObjects.Add(xlSrcRange, Range("Obr_F.Av!$A$5:$" & textC & "$" & NR), , xlYes).Name = _
        "Tabla_Fil_Avan_Obr"
End Sub

Sub Borrar()
Attribute Borrar.VB_ProcData.VB_Invoke_Func = " \n14"
' Borrar Macro

    ' Borrar tabla de empleados
    Sheets("Emp_F.Av").ListObjects("Tabla_Fil_Avan_Emp").Range.Delete
   
    ' Borrar tabla de obreros
    Sheets("Obr_F.Av").ListObjects("Tabla_Fil_Avan_Obr").Range.Delete
       
End Sub

Sub Resul()

' Filtro de Resultados
'
' Observaciones:
'   * &: junta cadenas de texto
'   * _: Salto de línea dentro de la macro
'       es decir la línea de código es dos líneas
'        para hacer legible el código.
'   * Dim: Declara la variable
'       con el formato:
'       Dim -(nombre de variable)- As -(Tipo de variable)-
' Declaración de variables
    Dim j As Integer
    Dim i As Integer
    Dim textFor As String

    '  ***Empleados***
      
    ' Bucle de j desde 1 hasta 50
    ' donde cada valor que toma j (entre 1 y 50)
    ' representa la pregunta j (P1 hasta P50)
    For j = 1 To 50
        ' Bucle de i desde 1 hasta 5
        ' donde cada valor que toma i (entre 1 y 5)
        ' representa el valor de la Escala Likert (de 1 hasta 5)
        For i = 1 To 5
            ' Genera el texto que se pondrá en la celda
            ' Correspondiendo a la pregunta
            ' y el valor de la escala likert
            ' es decir, los valores de j e i
            textFor = "=COUNTIF(Tabla_Fil_Avan_Emp[" & CStr(j) & "]," & _
                    "R" & CStr(2) & _
                    "C" & CStr(i + 1) & ")"
            ' Inserta el texto de la variable textFor
            ' como fórmula en el formato R1C1 (Rows,Columns)
            ' en la celda correspondiente a la pregunta
            ' y el valor de la escala likert
            ' es decir, los valores de j e i
            Sheets("Resultados_F.Av").Cells(j + 2, i + 1).FormulaR1C1 = textFor
        Next
    Next
    
    ' ***Obreros***
    
    ' Bucle de j desde 1 hasta 50
    ' donde cada valor que toma j (entre 1 y 50)
    ' representa la pregunta j (P1 hasta P50)
    For j = 1 To 50
        ' Bucle de i desde 1 hasta 5
        ' donde cada valor que toma i (entre 1 y 5)
        ' representa el valor de la Escala Likert (de 1 hasta 5)
        For i = 1 To 5
            ' Genera el texto que se pondrá en la celda
            ' Correspondiendo a la pregunta
            ' y el valor de la escala likert
            ' es decir, los valores de j e i
            textFor = "=COUNTIF(Tabla_Fil_Avan_Obr[" & CStr(j) & "]," & _
                    "R" & CStr(2) & _
                    "C" & CStr(i + 15) & ")"
            ' Inserta el texto de la variable textFor
            ' como fórmula en el formato R1C1 (Rows,Columns)
            ' en la celda correspondiente a la pregunta
            ' y el valor de la escala likert
            ' es decir, los valores de j e i
            Sheets("Resultados_F.Av").Cells(j + 2, i + 15).FormulaR1C1 = textFor
        Next
    Next
End Sub
