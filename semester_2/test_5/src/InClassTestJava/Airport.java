package InClassTestJava;

import Support.Attribute;
import java.util.*;

public class Airport {

    private ArrayList<Aeroplane> landedAeroplanes;

    public Airport() {
        landedAeroplanes = new ArrayList<Aeroplane>();
    }

    public void addAeroplane(String name, String id, int passengerCount, int currentFuelLevel, int seatsOnPlane) {
        Aeroplane myPlane = new Aeroplane(name, id, passengerCount, currentFuelLevel, seatsOnPlane);
        landedAeroplanes.add(myPlane);
    }

    public void setFuelCapacity() {
        for (Aeroplane myPlane : landedAeroplanes) {
            myPlane.setFuelCapacity();
        }
    }

    public void refuel(int index) {
        Aeroplane myPlane = this.landedAeroplanes.get(index);
        myPlane.refuel();
    }

    public void disembark(String id, int passengersDisembarking) {
        for (Aeroplane myPlane : landedAeroplanes) {
            if (myPlane.getId() == id) {
                myPlane.disembark(passengersDisembarking);
            }
        }
    }

    public int getCount() {
        return this.landedAeroplanes.size();
    }

    public String displayItem(int index) {
        String strValue = "\n";
        strValue += displayItem(index, Attribute.NAME_ID) + "\n";//"COMPANY: " + myPlane.getName() + ", ";        
        strValue += displayItem(index, Attribute.SEATS_PASSENGERS) + "\n";
        strValue += displayItem(index, Attribute.FUEL_CAPACITY) + "";
        return strValue;
    }

    public String displayItem(int index, Attribute selAttribute) {
        Aeroplane myPlane = this.landedAeroplanes.get(index);
        String sInfo = "";
        switch (selAttribute) {
            case NAME_ID:
                sInfo = "NAME: " + myPlane.getName();
                sInfo += ", ID: " + myPlane.getId();
                break;
            case SEATS_PASSENGERS:
                sInfo = "SEATS: " + myPlane.getSeats() + ",  PASSENGERS: " + myPlane.getPassengers();
                break;
            case FUEL_CAPACITY:
                sInfo = "FUEL: " + myPlane.getFuel();
                if (myPlane.getFuelCapacity() <= 0) {
                    sInfo += ",  CAPACITY:" + " ***NOT SET*** ";
                } else {
                    sInfo += ",  CAPACITY: " + myPlane.getFuelCapacity();
                }
                break;
        }
        return sInfo;
    }
}
