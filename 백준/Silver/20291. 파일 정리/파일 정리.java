import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static String[] data;
    static Map<String, Integer> map = new HashMap<>();
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());



        for(int i = 0; i<n; i++){
            String tmp = br.readLine();
            String[] tmpStrings = tmp.split("\\.");

            if(map.containsKey(tmpStrings[1])){
                map.put(tmpStrings[1], map.get(tmpStrings[1]) + 1);
            }else{
                map.put(tmpStrings[1], 1);
            }
        }

        ArrayList<String> keySet = new ArrayList<>(map.keySet());
        Collections.sort(keySet, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                return s1.compareTo(s2);
            }
        });

        for(String key: keySet){
            System.out.println(key + " " + map.get(key));
        }
    }
}