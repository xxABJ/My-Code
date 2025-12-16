<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()>
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()>
    Protected Overrides Sub Dispose(disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()>
    Private Sub InitializeComponent()
        btnFirst = New Button()
        btnSecond = New Button()
        btnVariable = New Button()
        btnDatatypes = New Button()
        SuspendLayout()
        ' 
        ' btnFirst
        ' 
        btnFirst.BackColor = Color.FromArgb(CByte(255), CByte(128), CByte(128))
        btnFirst.Location = New Point(32, 98)
        btnFirst.Name = "btnFirst"
        btnFirst.Size = New Size(176, 87)
        btnFirst.TabIndex = 0
        btnFirst.Text = "My First Button"
        btnFirst.UseVisualStyleBackColor = False
        ' 
        ' btnSecond
        ' 
        btnSecond.BackColor = Color.FromArgb(CByte(255), CByte(255), CByte(128))
        btnSecond.Location = New Point(153, 256)
        btnSecond.Name = "btnSecond"
        btnSecond.Size = New Size(216, 65)
        btnSecond.TabIndex = 1
        btnSecond.Text = "My Second Button"
        btnSecond.UseVisualStyleBackColor = False
        ' 
        ' btnVariable
        ' 
        btnVariable.BackColor = Color.FromArgb(CByte(128), CByte(255), CByte(128))
        btnVariable.Location = New Point(391, 59)
        btnVariable.Name = "btnVariable"
        btnVariable.Size = New Size(186, 126)
        btnVariable.TabIndex = 2
        btnVariable.Text = "My Variable Button"
        btnVariable.UseVisualStyleBackColor = False
        ' 
        ' btnDatatypes
        ' 
        btnDatatypes.BackColor = Color.FromArgb(CByte(128), CByte(255), CByte(255))
        btnDatatypes.Location = New Point(574, 269)
        btnDatatypes.Name = "btnDatatypes"
        btnDatatypes.Size = New Size(133, 125)
        btnDatatypes.TabIndex = 3
        btnDatatypes.Text = "Datatypes Button"
        btnDatatypes.UseVisualStyleBackColor = False
        ' 
        ' Buttons
        ' 
        AutoScaleDimensions = New SizeF(7F, 15F)
        AutoScaleMode = AutoScaleMode.Font
        ClientSize = New Size(800, 450)
        Controls.Add(btnDatatypes)
        Controls.Add(btnVariable)
        Controls.Add(btnSecond)
        Controls.Add(btnFirst)
        Name = "Buttons"
        Text = "Form1"
        ResumeLayout(False)
    End Sub

    Friend WithEvents btnFirst As Button
    Friend WithEvents btnSecond As Button
    Friend WithEvents btnVariable As Button
    Friend WithEvents btnDatatypes As Button

End Class
