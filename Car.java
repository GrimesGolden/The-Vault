public class Car extends Vehicle implements Maintainable
{	

	private int number_of_cylinders;
	private float cost_per_cylinder_per_hour = 5;
	// New private int to store cost per hour. 

	public Car(String name, int speed, int cylinders, float cost_per_cylinder_per_hour)
	// Calls parent constructor to give name and speed 
	{
		super(name, speed);
		number_of_cylinders = cylinders;
	}

	public float runningCost(int hours_of_operation)
	// Abstracted from Vehicle class.
	{
		float running_cost = (hours_of_operation * cost_per_cylinder_per_hour * number_of_cylinders);
		return running_cost;
	}

	public float maintenanceCost(float cost_Per_Unit)
	// Implemented from maintenance.
	{
		float cost = cost_Per_Unit * number_of_cylinders;
		return cost;
	}

	public void setCylinders(int cylinders)
	{
		number_of_cylinders = cylinders;
	}

	public int getCylinders()
	{
		return number_of_cylinders;
	}

	public String toString()
	{
		String message = "Name: " + this.getName() + 
		"\nMax Speed: " + this.getSpeed() + 
		"\nNum. Of Cylinders: " + this.getCylinders() +
		"\nCost Per Cylinder: " + cost_per_cylinder_per_hour;

		return message;
	}

}