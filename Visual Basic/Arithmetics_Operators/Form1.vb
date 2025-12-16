Public Class Form1

	Private Sub buttonEquals_Click(sender As Object, e As EventArgs) Handles buttonEquals.Click

		Dim decNum1 As Decimal
		Dim decNum2 As Decimal
		Dim strOperator As String
		Dim decResult As Decimal

		If textboxNumber1.Text = "" Or textboxNumber2.Text = "" Then
			MsgBox("Can not leave a box empty :)")
			Exit Sub
		End If

		decNum1 = Convert.ToDecimal(textboxNumber1.Text)
		decNum2 = Convert.ToDecimal(textboxNumber2.Text)
		strOperator = listboxOperators.SelectedIndex

		Select Case strOperator ' Selected operator based on index of items in listbox
			Case 0 ' Addition (+)
				decResult = decNum1 + decNum2

			Case 1 ' Subtraction (-)
				decResult = decNum1 - decNum2

			Case 2 ' Multiplication (*)
				decResult = decNum1 * decNum2

			Case 3 ' Division (/)
				If decNum1 = 0 Or decNum2 = 0 Then
					MsgBox("Can not divid by zero !")
					Exit Sub
				End If
				decResult = decNum1 / decNum2

			Case 4 ' Power (^)
				decResult = decNum1 ^ decNum2

			Case 5 ' Integer Division (\)
				decResult = decNum1 \ decNum2

			Case 6 ' Mod (Mod)
				decResult = decNum1 Mod decNum2

			Case Else
				MsgBox("Please select a operator.")
				Exit Sub

		End Select

		textboxAnswer.Text = decResult

		'BO(DM)(AS) - Brakets, Orders, Division/Multiplication, Addition/Subtraction

	End Sub

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load

        MsgBox("This is a program demonstrating arithmetic operators !")

    End Sub

End Class
