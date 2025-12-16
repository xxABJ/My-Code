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
        btnUserInput = New Button()
        labelFirstName = New Label()
        textboxFirstName = New TextBox()
        textboxLastName = New TextBox()
        labelLastName = New Label()
        textboxGender = New TextBox()
        labelGender = New Label()
        buttonNameInput = New Button()
        listboxOccupation = New ListBox()
        labelOccupation = New Label()
        SuspendLayout()
        ' 
        ' btnUserInput
        ' 
        btnUserInput.BackColor = Color.FromArgb(CByte(128), CByte(128), CByte(255))
        btnUserInput.Location = New Point(55, 171)
        btnUserInput.Name = "btnUserInput"
        btnUserInput.Size = New Size(133, 64)
        btnUserInput.TabIndex = 0
        btnUserInput.Text = "User Input Button"
        btnUserInput.UseVisualStyleBackColor = False
        ' 
        ' labelFirstName
        ' 
        labelFirstName.AutoSize = True
        labelFirstName.Location = New Point(269, 64)
        labelFirstName.Name = "labelFirstName"
        labelFirstName.Size = New Size(70, 15)
        labelFirstName.TabIndex = 1
        labelFirstName.Text = "First Name :"
        ' 
        ' textboxFirstName
        ' 
        textboxFirstName.Location = New Point(345, 61)
        textboxFirstName.Name = "textboxFirstName"
        textboxFirstName.Size = New Size(160, 23)
        textboxFirstName.TabIndex = 2
        ' 
        ' textboxLastName
        ' 
        textboxLastName.Location = New Point(344, 102)
        textboxLastName.Name = "textboxLastName"
        textboxLastName.Size = New Size(160, 23)
        textboxLastName.TabIndex = 4
        ' 
        ' labelLastName
        ' 
        labelLastName.AutoSize = True
        labelLastName.Location = New Point(269, 110)
        labelLastName.Name = "labelLastName"
        labelLastName.Size = New Size(69, 15)
        labelLastName.TabIndex = 3
        labelLastName.Text = "Last Name :"
        ' 
        ' textboxGender
        ' 
        textboxGender.Location = New Point(345, 147)
        textboxGender.Name = "textboxGender"
        textboxGender.Size = New Size(160, 23)
        textboxGender.TabIndex = 6
        ' 
        ' labelGender
        ' 
        labelGender.AutoSize = True
        labelGender.Location = New Point(269, 155)
        labelGender.Name = "labelGender"
        labelGender.Size = New Size(51, 15)
        labelGender.TabIndex = 5
        labelGender.Text = "Gender :"
        ' 
        ' buttonNameInput
        ' 
        buttonNameInput.BackColor = Color.FromArgb(CByte(128), CByte(255), CByte(128))
        buttonNameInput.Location = New Point(578, 185)
        buttonNameInput.Name = "buttonNameInput"
        buttonNameInput.Size = New Size(195, 68)
        buttonNameInput.TabIndex = 7
        buttonNameInput.Text = "Press after filling!"
        buttonNameInput.UseVisualStyleBackColor = False
        ' 
        ' listboxOccupation
        ' 
        listboxOccupation.FormattingEnabled = True
        listboxOccupation.Items.AddRange(New Object() {"Bus Driver", "Teacher", "Soilder", "Farmer", "Coach"})
        listboxOccupation.Location = New Point(323, 213)
        listboxOccupation.Name = "listboxOccupation"
        listboxOccupation.Size = New Size(139, 139)
        listboxOccupation.TabIndex = 8
        ' 
        ' labelOccupation
        ' 
        labelOccupation.AutoSize = True
        labelOccupation.Location = New Point(323, 195)
        labelOccupation.Name = "labelOccupation"
        labelOccupation.Size = New Size(140, 15)
        labelOccupation.TabIndex = 9
        labelOccupation.Text = "Choose your occupation:"
        ' 
        ' Form1
        ' 
        AutoScaleDimensions = New SizeF(7F, 15F)
        AutoScaleMode = AutoScaleMode.Font
        ClientSize = New Size(800, 450)
        Controls.Add(labelOccupation)
        Controls.Add(listboxOccupation)
        Controls.Add(buttonNameInput)
        Controls.Add(textboxGender)
        Controls.Add(labelGender)
        Controls.Add(textboxLastName)
        Controls.Add(labelLastName)
        Controls.Add(textboxFirstName)
        Controls.Add(labelFirstName)
        Controls.Add(btnUserInput)
        Name = "Form1"
        Text = "Form1"
        ResumeLayout(False)
        PerformLayout()
    End Sub

    Friend WithEvents btnUserInput As Button
    Friend WithEvents labelFirstName As Label
    Friend WithEvents textboxFirstName As TextBox
    Friend WithEvents textboxLastName As TextBox
    Friend WithEvents labelLastName As Label
    Friend WithEvents textboxGender As TextBox
    Friend WithEvents labelGender As Label
    Friend WithEvents buttonNameInput As Button
    Friend WithEvents listboxOccupation As ListBox
    Friend WithEvents labelOccupation As Label

End Class
