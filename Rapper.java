import javax.swing.*; // Imports java swing capability for JFrame etc..
import java.awt.event.*; // Imports event handling.
import java.util.ArrayList;
import java.util.Random;

public class Rapper extends JFrame
{	
	private JPanel panel; // Creates a panel variable.
	private JTextField textField; // Creates a text field variable
	private JButton button; // Creates a reference variable to a JButton object.
	private final int WINDOW_WIDTH = 650; // Final int for width
	private final int WINDOW_HEIGHT = 300; //Final width for height. 

	public Rapper()
	// Constructor for the IncDec class, a child of the JFrame class. A JFrame object.
	{

		setTitle("Choose Your Rapper Name!"); // Sets the title.

		setSize(WINDOW_WIDTH, WINDOW_HEIGHT); // Sets size using instance variables.

		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //Sets a default exit on close.

		buildPanel(); // Utilize the buildPanel()

		add(panel); // Add built JPanel object panel to the JFrame

		setVisible(true); // It should be visible. 
		
	}

	private void buildPanel()
	{
		textField = new JTextField(25); // Create a small text field.
		button = new JButton("Get Rapper Name"); // Create a button;
		textField.setText("Your Rapper Name"); // Add the text;

		// Add action listeners to buttons.
		button.addActionListener(new buttonListener()); // Add an action listener to the button.
	
		panel = new JPanel(); // Panel now references a new JPanel object.

		panel.add(button); // Add incButton to the panel.
		panel.add(textField); // Add text field to the panel.
	}

	public static String rapperName()
	{
		ArrayList<String> firstNames = new ArrayList<String>();
		ArrayList<String> lastNames = new ArrayList<String>();
		Random randomNumber = new Random();

		firstNames.add("A$AP");
		firstNames.add("Yung");
		firstNames.add("Post");
		firstNames.add("Danny");
		firstNames.add("Johnny");
		firstNames.add("Gains");
		firstNames.add("Richard");
		firstNames.add("Ratchet");
		firstNames.add("Creatine");

		lastNames.add("Johnson");
		lastNames.add("McKenzie");
		lastNames.add("Toenail");
		lastNames.add("Gainstown");
		lastNames.add("Lampshade");
		lastNames.add("Jackson");
		lastNames.add("Fasthands");
		lastNames.add("MaLone");

		int randomFirst = randomNumber.nextInt(firstNames.size());
		int randomLast = randomNumber.nextInt(firstNames.size());

		String message = "Your rapper name is: " + firstNames.get(randomFirst) + " " + lastNames.get(randomLast);
		return message;
	}



	private class buttonListener implements ActionListener
	// buttonListener is action listener class for the button.
	// Utilizes the ActionListener interface, therefore it must contain the actionPerformed method, which takes an ActionEvent parameter. 
	{
		
		public void actionPerformed(ActionEvent e)
		// actionPerformed() executes when the user clicks on increment button.
		{	
			try
			{
				// Obtain current rapper name using method.
    			String message = rapperName();

    			// Set text of field to rapper name.
    			textField.setText(message);
			}
			catch(NumberFormatException i)
			// Will catch a number format exception, in this case the exception being the text field data was null (nothing there).
			{
				textField.setText("enter a number please");
			}
			
		}
	}

	public static void main(String[] args)
	{
		new Rapper();
	}
}

	