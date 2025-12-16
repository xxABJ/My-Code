Public Class Form1

    Private Sub btnFirst_Click(sender As Object, e As EventArgs) Handles btnFirst.Click

        MsgBox("This is my first button!")
        MsgBox("See you !")

    End Sub

    Private Sub btnSecond_Click(sender As Object, e As EventArgs) Handles btnSecond.Click

        MessageBox.Show("This is my second button!")
        MessageBox.Show("Goodbye !")

    End Sub

    Private Sub btnVariable_Click(sender As Object, e As EventArgs) Handles btnVariable.Click

        Dim stFirstname As String
        Dim stLastname As String

        stFirstname = "Ali"
        stLastname = "Al-Mansouri"

        MsgBox("My name is " & stFirstname & " " & stLastname & " and this is a Variable Button!")

        stFirstname = "x"
        stLastname = "ABJ"

        MsgBox("My name is " & stFirstname & " " & stLastname & " and the value of the same Variables has been changed!")

    End Sub

    <Obsolete>
    Private Sub btnDatatypes_Click(sender As Object, e As EventArgs) Handles btnDatatypes.Click

        Dim stBrand As String
        Dim stModel As String
        Dim inManufacturingYear As Integer
        Dim decPrice As Decimal
        Dim blInsurace As Boolean
        Dim dtAvailableSince As Date

        stBrand = "Toyota"
        stModel = "Land Cruiser"
        inManufacturingYear = 2020
        decPrice = 250000.59
        blInsurace = False
        dtAvailableSince = #11/21/2025#

        MsgBox("This is a button that obtains different types of datatype variables !")
        MsgBox("Car Brand: " & stBrand & vbNewLine & "(String)" & vbNewLine & vbNewLine &
               "Car Model: " & stModel & vbNewLine & "(String)" & vbNewLine & vbNewLine &
               "Manufacturing Year: " & inManufacturingYear & vbNewLine & "(Integer)" & vbNewLine & vbNewLine &
               "Price: " & decPrice & " QR!" & vbNewLine & "(Decimal)" & vbNewLine & vbNewLine &
               "Is Insured: " & blInsurace & vbNewLine & "(Boolean)" & vbNewLine & vbNewLine &
               "Available Since: " & dtAvailableSince & vbNewLine & "(Data)")

    End Sub


End Class