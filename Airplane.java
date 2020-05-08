public class Airplane extends Vehicle implements Maintainable
{
	
	private int number_of_engines;
	private float cost_per_engines_per_hour = 50;

	public Airplane(String name, int speed, int engines, float cost_per_engines_per_hour)
	{
		super(name, speed);
		number_of_engines = engines;
	}

	public float runningCost(int hours_of_operation)
	// Abstracted from Vehicle class.
	{
		float running_cost = (hours_of_operation * cost_per_engines_per_hour * number_of_engines);
		return running_cost;
	}

	public float maintenanceCost(float cost_Per_Unit)
	// Implemented from maintenance.
	{
		float cost = cost_Per_Unit * number_of_engines;
		return cost;
	}


	public void setEngines(int engines)
	{
		number_of_engines = engines;
	}

	public int getEngines()
	{
		return number_of_engines;
	}

	public String toString()
	{
		String message = "Name: " + this.getName() + 
		"\nMax Speed: " + this.getSpeed() + 
		"\nNum. Of Engines: " + this.getEngines() +
		"\nCost Per Engine: " + cost_per_engines_per_hour;

		return message;
	}
}
