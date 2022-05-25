class Calculate:
    # current unit prices for residential area 25-05-2022
    f50u = 3.20  # first 50 unit price
    s50u = 3.65  # second 50 unit price
    t150u = 4.25  # third 150 unit price
    a250u = 5.05  # above 250 unit price

    def calculateTorrentEnergyBill(self, unit):
        # calculate for the first consumed 50 units
        if unit >= 50:
            firstFifty = 50 * self.f50u
            print("Your Fist 50 unit Bill is => ", firstFifty)
            left1 = unit - 50
            print(f"Left-1 Unit {unit} - 50 => ", left1)
            print("------------------------------------------------------------")
            if left1 == 0:
                print(f"Your Total {unit} unit's Energy Bill is => ", firstFifty)
            elif left1 < 50:
                secondLastBill = left1 * self.s50u
                print(f"Your Left {left1} unit Bill is => ", secondLastBill)
                print("------------------------------------------------------------")
                finalBill = firstFifty + secondLastBill
                print(f"Your Total {unit} unit's Energy Bill is => ", finalBill)

            # calculate for the second consumed 50 units
            if left1 >= 50:
                secondFifty = 50 * self.s50u
                print("Your Second 50 unit Bill is => ", secondFifty)
                left2 = left1 - 50
                print(f"Left-2 Unit {left1} - 50 => ", left2)
                print("------------------------------------------------------------")
                if left2 == 0:
                    finalBill = firstFifty + secondFifty
                    print("Your Total Energy Bill is => ", finalBill)
                elif left2 < 50:
                    secondLastBill = left2 * self.t150u
                    print(f"Your Left {left2} unit Bill is => ", secondLastBill)
                    print("------------------------------------------------------------")
                    finalBill = firstFifty + secondFifty + secondLastBill
                    print("Your Total Energy Bill is => ", finalBill)

                # calculate for the third consumed 150 units
                if left2 >= 150:
                    thirdOneFifty = 150 * self.t150u
                    print("Your Third 150 unit Bill is => ", thirdOneFifty)
                    left3 = left2 - 150
                    print(f"Left-3 Unit {left2} - 150 => ", left3)
                    print("------------------------------------------------------------")
                    if left3 == 0:
                        finalBill = firstFifty + secondFifty + thirdOneFifty
                        print("Your Total Energy Bill is => ", finalBill)

                    # calculate for the forth and last consumed above 250 units
                    if left3 >= 250:
                        aboveTwoFifty = left3 * self.a250u
                        print(f"Your Final {left3} unit Bill is => ", aboveTwoFifty)
                        left4 = left3 - left3
                        print(f"Left-4 Unit {left3} - {left3}", left4)
                        print("------------------------------------------------------------")
                        if left4 == 0:
                            finalBill = firstFifty + secondFifty + thirdOneFifty + aboveTwoFifty
                            print("Your Total Energy Bill is => ", finalBill)
                        else:
                            print("nothing")

                    else:
                        secondLastBill = left3 * self.a250u
                        print(f"Your Left {left3} unit Bill is => ", secondLastBill)
                        print("------------------------------------------------------------")
                        finalBill = firstFifty + secondFifty + thirdOneFifty + secondLastBill
                        print("Your Total Energy Bill is => ", finalBill)

                else:
                    secondLastBill = left2 * self.t150u
                    print(f"Your Left {left2} unit Bill is => ", secondLastBill)
                    print("------------------------------------------------------------")
                    finalBill = firstFifty + secondFifty + secondLastBill
                    print("Your Total Energy Bill is => ", finalBill)

        else:
            finalBill = unit * self.f50u
            print(f"Your {unit} unit's Energy Bill is => ", finalBill)
