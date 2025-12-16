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
        listboxOperators = New ListBox()
        labelOperators = New Label()
        textboxNumber1 = New TextBox()
        labelNumber1 = New Label()
        labelNumber2 = New Label()
        textboxNumber2 = New TextBox()
        buttonEquals = New Button()
        textboxAnswer = New TextBox()
        labelAnswer = New Label()
        SuspendLayout()
        ' 
        ' listboxOperators
        ' 
        listboxOperators.DisplayMember = "0 = +, "
        listboxOperators.FormattingEnabled = True
        listboxOperators.Items.AddRange(New Object() {"Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)", "Power (^)", "Integer Division (\)", "Mod (Mod)"})
        listboxOperators.Location = New Point(215, 63)
        listboxOperators.Name = "listboxOperators"
        listboxOperators.Size = New Size(108, 124)
        listboxOperators.TabIndex = 0
        ' 
        ' labelOperators
        ' 
        labelOperators.AutoSize = True
        labelOperators.Location = New Point(238, 45)
        labelOperators.Name = "labelOperators"
        labelOperators.Size = New Size(59, 15)
        labelOperators.TabIndex = 1
        labelOperators.Text = "Operators"
        ' 
        ' textboxNumber1
        ' 
        textboxNumber1.Location = New Point(45, 110)
        textboxNumber1.Name = "textboxNumber1"
        textboxNumber1.Size = New Size(132, 23)
        textboxNumber1.TabIndex = 2
        ' 
        ' labelNumber1
        ' 
        labelNumber1.AutoSize = True
        labelNumber1.Location = New Point(83, 77)
        labelNumber1.Name = "labelNumber1"
        labelNumber1.Size = New Size(60, 15)
        labelNumber1.TabIndex = 3
        labelNumber1.Text = "Number 1"
        ' 
        ' labelNumber2
        ' 
        labelNumber2.AutoSize = True
        labelNumber2.Location = New Point(400, 77)
        labelNumber2.Name = "labelNumber2"
        labelNumber2.Size = New Size(60, 15)
        labelNumber2.TabIndex = 5
        labelNumber2.Text = "Number 2"
        ' 
        ' textboxNumber2
        ' 
        textboxNumber2.Location = New Point(362, 110)
        textboxNumber2.Name = "textboxNumber2"
        textboxNumber2.Size = New Size(132, 23)
        textboxNumber2.TabIndex = 4
        ' 
        ' buttonEquals
        ' 
        buttonEquals.BackColor = Color.FromArgb(CByte(192), CByte(255), CByte(192))
        buttonEquals.Font = New Font("Segoe UI", 27.75F, FontStyle.Regular, GraphicsUnit.Point, CByte(0))
        buttonEquals.Location = New Point(553, 91)
        buttonEquals.Name = "buttonEquals"
        buttonEquals.Size = New Size(103, 66)
        buttonEquals.TabIndex = 6
        buttonEquals.Text = "="
        buttonEquals.TextAlign = ContentAlignment.TopCenter
        buttonEquals.UseVisualStyleBackColor = False
        ' 
        ' textboxAnswer
        ' 
        textboxAnswer.Location = New Point(83, 317)
        textboxAnswer.Name = "textboxAnswer"
        textboxAnswer.Size = New Size(625, 23)
        textboxAnswer.TabIndex = 7
        ' 
        ' labelAnswer
        ' 
        labelAnswer.AutoSize = True
        labelAnswer.Location = New Point(83, 299)
        labelAnswer.Name = "labelAnswer"
        labelAnswer.Size = New Size(49, 15)
        labelAnswer.TabIndex = 8
        labelAnswer.Text = "Answer:"
        ' 
        ' Form1
        ' 
        AutoScaleDimensions = New SizeF(7F, 15F)
        AutoScaleMode = AutoScaleMode.Font
        ClientSize = New Size(800, 450)
        Controls.Add(labelAnswer)
        Controls.Add(textboxAnswer)
        Controls.Add(buttonEquals)
        Controls.Add(labelNumber2)
        Controls.Add(textboxNumber2)
        Controls.Add(labelNumber1)
        Controls.Add(textboxNumber1)
        Controls.Add(labelOperators)
        Controls.Add(listboxOperators)
        Name = "Form1"
        Text = "Form1"
        ResumeLayout(False)
        PerformLayout()
    End Sub

    Friend WithEvents listboxOperators As ListBox
    Friend WithEvents labelOperators As Label
    Friend WithEvents textboxNumber1 As TextBox
    Friend WithEvents labelNumber1 As Label
    Friend WithEvents labelNumber2 As Label
    Friend WithEvents textboxNumber2 As TextBox
    Friend WithEvents buttonEquals As Button
    Friend WithEvents textboxAnswer As TextBox
    Friend WithEvents labelAnswer As Label

End Class
