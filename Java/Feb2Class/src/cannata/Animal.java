package cannata;

/**
 * Created by pcannata on 2/2/16.
 */
public class Animal {
    private  static boolean alive;
    public void setAlive(boolean a) { alive = a;}
    public boolean getAlive() {return alive;}

    private int numOfLegs;
    public void setNumOfLegs(int numOfLegs) {this.numOfLegs = numOfLegs;}
    public int getNumOfLegs() {return numOfLegs;}

    public Animal(int numOfLegs){
        this.numOfLegs = numOfLegs;
    }
    public Animal(int numOfLegs, boolean alive){
        this.numOfLegs = numOfLegs + 10;
        this.alive = alive;
    }
}
