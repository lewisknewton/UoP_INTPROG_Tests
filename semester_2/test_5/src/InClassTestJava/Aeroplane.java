package InClassTestJava;

public class Aeroplane {

    private String name;
    private String id;
    private double fuelCapacity;
    private int seats;

    private int passengers;
    private double fuel;

    public Aeroplane(String name, String id, int passengerCount, double currentFuel, int availableSeats) {
        this.name = name;
        this.id = id;
        this.seats = availableSeats;
        this.passengers = passengerCount;
        this.fuel = currentFuel;
    }

    public String getName() {
        return name;
    }

    public String getId() {
        return id;
    }

    public int getPassengers() {
        return passengers;
    }

    public double getFuel() {
        return fuel;
    }

    public double getSeats() {
        return seats;
    }

    public double getFuelCapacity() {
        return fuelCapacity;
    }

    public void setFuelCapacity() {
        fuelCapacity = seats * 90;
    }

    public void disembark(int passengersDisembarking) {
        passengers -= passengersDisembarking;
    }

    public void refuel() {
        if ((fuel + 100) <= fuelCapacity) {
            fuel += 100;
        }
    }
}
