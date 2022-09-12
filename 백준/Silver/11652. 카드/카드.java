import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static String key;
    static int value;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        Map<String, Integer> map = new HashMap<>();
        for(int i = 0; i<n; i++){
            key = br.readLine();
            if(map.containsKey(key)){
                value = map.get(key);
                map.put(key, value + 1);
            }else{
                map.put(key, 1);
            }
        }

        List<String> keySet = new ArrayList<>(map.keySet());
        keySet.sort(new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {


                if(map.get(o1).equals(map.get(o2))){
                    return Long.valueOf(Long.parseLong(o1)).compareTo(Long.parseLong(o2));

                }else{
                    return -(map.get(o1).compareTo(map.get(o2)));
                }
            }
        });
        System.out.println(Long.parseLong(keySet.get(0)));

    }
}