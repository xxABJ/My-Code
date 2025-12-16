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
        buttonGrade = New Button()
        textboxScore = New TextBox()
        labelScore = New Label()
        SuspendLayout()
        ' 
        ' buttonGrade
        ' 
        buttonGrade.Location = New Point(61, 145)
        buttonGrade.Name = "buttonGrade"
        buttonGrade.Size = New Size(200, 96)
        buttonGrade.TabIndex = 0
        buttonGrade.Text = "Get Grade!"
        buttonGrade.UseVisualStyleBackColor = True
        ' 
        ' textboxScore
        ' 
        textboxScore.Location = New Point(100, 89)
        textboxScore.MaxLength = 3
        textboxScore.Name = "textboxScore"
        textboxScore.Size = New Size(126, 23)
        textboxScore.TabIndex = 1
        ' 
        ' labelScore
        ' 
        labelScore.AutoSize = True
        labelScore.Location = New Point(100, 51)
        labelScore.Name = "labelScore"
        labelScore.Size = New Size(126, 15)
        labelScore.TabIndex = 2
        labelScore.Text = "Enter your exam score!"
        ' 
        ' Form1
        ' 
        AutoScaleDimensions = New SizeF(7F, 15F)
        AutoScaleMode = AutoScaleMode.Font
        ClientSize = New Size(327, 297)
        Controls.Add(labelScore)
        Controls.Add(textboxScore)
        Controls.Add(buttonGrade)
        Name = "Form1"
        Text = "Form1"
        ResumeLayout(False)
        PerformLayout()
    End Sub

    Friend WithEvents buttonGrade As Button
    Friend WithEvents textboxScore As TextBox
    Friend WithEvents labelScore As Label

End Class
