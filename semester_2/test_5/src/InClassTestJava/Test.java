package InClassTestJava;

public class Test {

    public static void main(String[] args) {

        System.out.println("******STEP 1 OBJECT CREATION************");
        Airport myAirport = new Airport();

        System.out.println("******STEP 2 ADD PLANES************");
        myAirport.addAeroplane("LazyJet", "LZ166", 100, 1600, 100);
        myAirport.addAeroplane("PedaloJet", "PDL77", 10, 100, 50);
        display(myAirport);

        System.out.println("\n******STEP 3 SET FUEL CAPACITY (90*SEATS)************");
        myAirport.setFuelCapacity();
        display(myAirport);

        System.out.println("\n******STEP 4 REFUEL PLANE 2 (+100)************");
        display(myAirport, 1);
        myAirport.refuel(1);
        display(myAirport, 1);

        System.out.println("\n** STEP 5 DISEMBARK 5 PASSENGERS from LZ166 **");
        display(myAirport, 0);
        myAirport.disembark("LZ166", 5);
        display(myAirport, 0);

    }

    public static void display(Airport myAirport, int planeIndex) {
        System.out.println(myAirport.displayItem(planeIndex));
    }

    public static void display(Airport myAirport) {
        for (int i = 0; i < myAirport.getCount(); i++) {
            System.out.println(myAirport.displayItem(i));
        }
    }

}
