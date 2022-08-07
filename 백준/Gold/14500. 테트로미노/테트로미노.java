import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n, m;
    static int max_value = 0;
    static List<Integer>[] data;

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] strings = br.readLine().split(" ");
        n = Integer.parseInt(strings[0]);
        m = Integer.parseInt(strings[1]);


        data = new List[n];


        for(int i = 0; i<n; i++){
            data[i] = new ArrayList<Integer>(m);
            strings = br.readLine().split(" ");
            for(int j = 0; j<m; j++){
                data[i].add(Integer.parseInt(strings[j]));
            }
        }


        for(int i = 0; i<n; i++){
            for(int j = 0; j<m; j++){
                ArrayList<Point> points = new ArrayList<>();
                points.add(new Point(i, j));

                dfs(3, i, j, data[i].get(j), points);
            }
        }

        System.out.println(max_value);
    }

    static void dfs(int cnt, int x, int y, int sum, ArrayList<Point> points){
        if(cnt > 0) {
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if(0 <= nx && nx < n && 0 <= ny && ny < m){

                    Point newPoint = new Point(nx, ny);
                    if(!points.contains(newPoint)){
                        ArrayList<Point> newPoints = new ArrayList<>();
                        Iterator<Point> it = points.iterator();
                        while(it.hasNext()){
                            newPoints.add(it.next());
                        }

                        newPoints.add(newPoint);
                        dfs(cnt - 1, x, y, sum + data[nx].get(ny), newPoints);
                        dfs(cnt - 1, nx, ny, sum + data[nx].get(ny), newPoints);
                    }
                }
            }
        } else{

            max_value = Math.max(sum, max_value);
        }
    }
    
    static class Point{
        int x;
        int y;

        public Point(int x, int y){
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {

            if(o != null && o instanceof Point) {
                Point p = (Point)o;
                if(p.x == this.x && p.y == this.y) {
                    return true;
                }
                return false;
            }
            return false;
        }
    }
}