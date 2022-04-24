public class Demo {
	public static void main(String[] args) {
    	System.loadLibrary("JavaToPySo");
        JavaToPySo jniToCpp = new JavaToPySo();
        jniToCpp.initModule();
        String result1 = jniToCpp.testFunction("root,root,192.168.0.89,3306,qqny,q_main,2021-09-01,2021-11-21");
        String result2 = jniToCpp.callentelectFunction("root,root,192.168.0.89,3306,qqny,q_main,2021-09-01,2021-11-21");
        jniToCpp.uninitModule();
        System.out.println(result1);
        System.out.println(result2);
    }
}
