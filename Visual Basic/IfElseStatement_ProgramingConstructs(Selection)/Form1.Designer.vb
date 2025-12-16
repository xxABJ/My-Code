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
        buttonGreet = New Button()
        textboxCountry = New TextBox()
        labelQuestion = New Label()
        SuspendLayout()
        ' 
        ' buttonGreet
        ' 
        buttonGreet.BackColor = SystemColors.ActiveCaptionText
        buttonGreet.ForeColor = SystemColors.ButtonFace
        buttonGreet.Location = New Point(277, 251)
        buttonGreet.Name = "buttonGreet"
        buttonGreet.Size = New Size(251, 120)
        buttonGreet.TabIndex = 0
        buttonGreet.Text = "Greet !"
        buttonGreet.UseVisualStyleBackColor = False
        ' 
        ' textboxCountry
        ' 
        textboxCountry.Location = New Point(275, 138)
        textboxCountry.Name = "textboxCountry"
        textboxCountry.Size = New Size(273, 23)
        textboxCountry.TabIndex = 1
        ' 
        ' labelQuestion
        ' 
        labelQuestion.AutoSize = True
        labelQuestion.Location = New Point(277, 109)
        labelQuestion.Name = "labelQuestion"
        labelQuestion.Size = New Size(123, 15)
        labelQuestion.TabIndex = 2
        labelQuestion.Text = "Where are you from? :"
        ' 
        ' Form1
        ' 
        AutoScaleDimensions = New SizeF(7F, 15F)
        AutoScaleMode = AutoScaleMode.Font
        ClientSize = New Size(800, 450)
        Controls.Add(labelQuestion)
        Controls.Add(textboxCountry)
        Controls.Add(buttonGreet)
        Name = "Form1"
        Text = "Form1"
        ResumeLayout(False)
        PerformLayout()
    End Sub

    Friend WithEvents buttonGreet As Button
    Friend WithEvents textboxCountry As TextBox
    Friend WithEvents labelQuestion As Label

End Class
