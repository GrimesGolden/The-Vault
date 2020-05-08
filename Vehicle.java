public abstract class Vehicle
// Abstract class vehicle will not be instantiated.
{
	private String name;
	private int max_speed;

	public Vehicle(String name, int max_speed)
	// Vehicle constructor
	{
		this.name = name;
		this.max_speed = max_speed;
	}

	public abstract float runningCost(int hours_of_operation);
	//abstract method to be overrun.

	public String getName()
	{
		return name;
	}

	public int getSpeed()
	{
		return max_speed;
	}

	public void setName(String name)
	{
		this.name = name;
	}

	public void setSpeed(int speed)
	{
		max_speed = speed;
	}

	public String toString()
	{
		String message = "Name: " + this.getName() + 
		"\nMax Speed: " + this.getSpeed();

		return message;
	}
	
}