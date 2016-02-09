package cannata;

public class Aristotle {

    public static void main(String[] args) {
        Animal a1 = new Animal(4, true);
        //a1.setNumOfLegs(4);
        //a1.setAlive(true);
        System.out.println("a1 numOfLegs is: " + a1.getNumOfLegs());
        System.out.println("a1 Alive is: " + a1.getAlive());

        Animal a2 = new Animal(37);
        //a2.setNumOfLegs(37);
        System.out.println("a2 numOfLegs is: " + a2.getNumOfLegs());
        System.out.println("a2 Alive is: " + a2.getAlive());

        a2.setAlive(false);
        System.out.println("a1 Alive is: " + a1.getAlive());
        System.out.println("a2 Alive is: " + a2.getAlive());

        Cat myCat = new Cat();
        myCat.setSound("Meow");
        System.out.println("myCat says: " + myCat.getSound());
        myCat.speak();

        // Examples of Polymorphism
        Human socrates = new Human();
        System.out.println("\nSocrates's animal is going to speak");
        socrates.animalSpeak(a1);
        System.out.println("\nSocrates's cat is going to speak");
        socrates.animalSpeak(myCat);

        Animal a3 = myCat;
        System.out.println("\nSocrates's cat is going to speak");
        socrates.animalSpeak(a3);

        // DOwncasting won't run
        /*
        Cat myCat1 = (Cat)a1;
        System.out.println("\nSocrates's cat is going to speak");
        socrates.animalSpeak(myCat1);
        */
    }
}
