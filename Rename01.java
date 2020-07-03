
// Java program to rename a file. 
import java.io.File; 
import java.io.*;
import java.lang.*;
  
public class test { 

    static boolean rename01(String dest,String nname){

        String str = dest; 
        String[] arrOfStr = str.split("/", 0); 
        int len=arrOfStr.length;

        String origin="";
        String last= arrOfStr[len-1];
        String ext=".";

        for (int i=0;i < last.length() ;++i ) {
            if(last.charAt(i) == '.')
                ext=".";
            else
                ext += last.charAt(i); 
        }

        for (int i=0;i < len-1 ;++i ) {
            origin += arrOfStr[i]+"/";
        }
        origin += nname + ext;

        File oldName1 = new File(dest); 
        File newName1 = new File(origin);

        if (oldName1.renameTo(newName1))  
            return true;
        else 
            return false;
        
    }

    public static void main(String[] args) 
    {  

        String path="/home/lx/Continue/mine2.jpg";
        String name="mine3";  

        if(rename01(path,name))
            System.out.println("Renamed successfully");         
        else 
            System.out.println("Error");
    } 
} 
