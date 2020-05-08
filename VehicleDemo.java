public class VehicleDemo
{
	public static void main(String[] args)
	{	
		// Create an instance of car and an instnce of an Airplane classes.
		Car car1 = new Car("Ford", 200, 6, 5);
		Airplane plane1 = new Airplane("Cessna", 180, 1, 100);


		// Calling all methods that are available to Car class && return value.
		System.out.println("All car methods: \n");
		System.out.println(car1.runningCost(24));
		System.out.println(car1.maintenanceCost(10));
		System.out.println(car1.getCylinders());
		System.out.println(car1);

		// Calling all methods that are available to Airplane class && return value.
		System.out.println("All plane methods: \n");
		System.out.println(plane1.runningCost(24));
		System.out.println(plane1.maintenanceCost(100));
		System.out.println(plane1.getEngines());
		System.out.println(plane1);

		// Define a reference variable of type Vehicle and assign it to car instance.
		Vehicle v1 = new Car("Dodge Challenger", 220, 8, 6);
		System.out.println("");
		System.out.println(v1);

		// We note that this printing v1 prints the toString() method of Car.java
		// This is due to the fact that the Car subclass overrides the toString method of car, therefore we revieve this now overidden method.


	}		
	
}