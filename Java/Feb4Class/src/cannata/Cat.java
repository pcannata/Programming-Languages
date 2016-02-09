package cannata;

/**
 * Created by pcannata on 2/4/16.
 */
public class Cat extends Animal {
    String sound;
    public void setSound(String s) { sound = s;}
    public String getSound() {return sound;}

    @Override
    public void speak(){
        System.out.println("I am a cat, and I say " + getSound());
    }
}
