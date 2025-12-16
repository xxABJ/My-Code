Public Class Form1
	Private Sub buttonGrade_Click(sender As Object, e As EventArgs) Handles buttonGrade.Click

		Dim iScore As Integer
		iScore = textboxScore.Text

		If IsNumeric(iScore) = True Then ' Check if input is numeric
			iScore = CInt(textboxScore.Text) ' Convert input to integer by using CInt(), if not used then  VB.NET will do it implicitly which might slow down performance

			If iScore >= 90 And iScore <= 100 Then
				MessageBox.Show("Your grade is A")
			ElseIf iScore >= 80 And iScore < 90 Then
				MessageBox.Show("Your grade is B")
			ElseIf iScore >= 70 And iScore < 80 Then
				MessageBox.Show("Your grade is C")
			ElseIf iScore >= 60 And iScore < 70 Then
				MessageBox.Show("Your grade is D")
			ElseIf iScore >= 50 And iScore < 60 Then
				MessageBox.Show("Your grade is E")
			ElseIf iScore >= 0 And iScore < 50 Then
				MessageBox.Show("Your grade is F")
			Else
				MessageBox.Show("Please enter a score between 0 and 100.")
				Exit Sub
			End If

		Else
			MessageBox.Show("Please enter a valid numeric score.")
			Exit Sub
		End If

		MessageBox.Show("Thank you for using the grading system." & vbNewLine &
						"You scored: " & iScore & " / 100 !")

		' Logical operators: And, Or, Not
		' Relational operators: =, <>, >, <, >=, <=
		' Arithmetic operators: +, -, *, /, \, Mod
		' Assignment operators: =
		' Concatenation operator: &

	End Sub

End Class
