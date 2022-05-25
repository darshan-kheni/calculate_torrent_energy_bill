from main import Calculate

Cal = Calculate()

# take numbers of unit consumed by the consumer
unit = int(input("Enter your total consumed unit: "))

Cal.calculateTorrentEnergyBill(unit)