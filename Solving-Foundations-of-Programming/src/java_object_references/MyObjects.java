package java_object_references;

// Object reference variables and addresses
// https://www.youtube.com/watch?v=EUCEx6j-7z4
public class MyObjects {
	public static void main(String[] args) {

		Object obj = new Object();
		
		System.out.println(obj);
		
		String foo = new String("Hello");
		String bar = new String("Bye");
		
		System.out.println(foo);
		System.out.println(bar);
		
		bar = foo;
		
		System.out.println(foo);
		System.out.println(bar);
	}
}
