Public Class Form1
    Private Sub btnUserInput_Click(sender As Object, e As EventArgs) Handles btnUserInput.Click

        Dim userInput As String

        userInput = InputBox("Please enter your name: ", "User Input")

        MsgBox("Hello, " & userInput & "! Welcome to the program.")

    End Sub

    Private Sub buttonNameInput_Click(sender As Object, e As EventArgs) Handles buttonNameInput.Click

        Dim stFirstName As String
        Dim stLastName As String
        Dim stGender As String
        Dim stOccupation As String

        stFirstName = textboxFirstName.Text
        stLastName = textboxLastName.Text
        stGender = textboxGender.Text
        stOccupation = listboxOccupation.SelectedItem

        MsgBox("Hello, " & stFirstName & " " & stLastName & "! You are a " & stGender & " " & stOccupation & "!")

    End Sub

	Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load

		listboxOccupation.Items.Add("Engineer")
		listboxOccupation.Items.Add("Doctor")
		listboxOccupation.Items.Add("Artist")

	End Sub


End Class
