package InClassTestJava;

public class Bus {

    private String company;
    private String id;
    private int passengers;
    private double currentDieselLevel;
    private double fuelTankSize;
    private int seats;

    public Bus(String companyName, String busId, int passengerCount) {
        company = companyName;
        id = busId;
        passengers = passengerCount;
    }

    public Bus(
            String companyName,
            String busId,
            int passengerCount,
            int availableSeats
    ) {
        company = companyName;
        id = busId;
        passengers = passengerCount;
        seats = availableSeats;
    }

    public void setCurrentDieselLevel(double dieselFromPump) {
        currentDieselLevel = dieselFromPump;
    }

    public void getOffBus(int passengersLeavingBus) {
        // Subtract those leaving bus from passengers member variable
        passengers -= passengersLeavingBus;
    }

    public String getCompanyName() {
        return company;
    }

    public String getId() {
        return id;
    }

    public int getPassengers() {
        return passengers;
    }

    public double getCurrentDieselLevel() {
        return currentDieselLevel;
    }

    public void setFuelTankSize(double max) {
        this.fuelTankSize = max;
    }

    public double getFuelTankSize() {
        return this.fuelTankSize;
    }

    public void refuelBus() {
        if ((currentDieselLevel + 10) < fuelTankSize) {
            // Add 10 to the current diesel level
            currentDieselLevel += 10;
        }
    }

    public void lastMinutePassengerPickup(int newPassengers) {
        if (currentDieselLevel > 10) {
            // Pick up passengers if there are enough seats
            if (newPassengers + passengers <= seats) {
                passengers += newPassengers;
            } else if (newPassengers + passengers > seats) {
                passengers = seats;
            }
        }
    }
}
