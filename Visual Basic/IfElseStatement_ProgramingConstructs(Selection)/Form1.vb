Public Class Form1
	Private Sub buttonGreet_Click(sender As Object, e As EventArgs) Handles buttonGreet.Click

		Dim stCountry As String
		stCountry = textboxCountry.Text

		If stCountry.ToUpper = "QATAR" Then
			MsgBox("Hala walla!")
		ElseIf stCountry.ToUpper = "EGYPT" Then
			MsgBox("Ahlan wa sahlan!")
		ElseIf stCountry.ToUpper = "FRANCE" Then
			MsgBox("Bonjour!")
		Else
			MsgBox("Hello my friend!")
			MsgBox("No condition for what you typed: " & stCountry & " !")
		End If

	End Sub

End Class
