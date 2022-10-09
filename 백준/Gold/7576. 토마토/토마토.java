import java.io.*;
import java.util.*;

public class Main {

    static StringTokenizer st;
    static int n, m, tmp, nx, ny, result;
    static int[][] data;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    static Queue<Point> queue = new LinkedList<>();

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        data = new int[n][m];
        for(int i = 0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j<m; j++){
                tmp = Integer.parseInt(st.nextToken());
                data[i][j] = tmp;
                if(tmp == 1){
                    queue.add(new Point(i, j));
                }
            }
        }

        bfs();

        result = 1;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(data[i][j] == 0){
                    result = 0;
                    break;
                }
                result = Math.max(result, data[i][j]);
            }
            if(result == 0){
                break;
            }
        }

        System.out.println(result - 1);
    }

    public static void bfs(){
        while(!queue.isEmpty()){
            Point point = queue.poll();
            int x = point.x;
            int y = point.y;
            for(int i = 0; i < 4; i++){
                nx = x + dx[i];
                ny = y + dy[i];

                if(0 <= nx && nx < n && 0 <= ny && ny < m){
                    if(data[nx][ny] == 0){
                        data[nx][ny] = data[x][y] + 1;
                        queue.add(new Point(nx, ny));
                    }
                }
            }
        }
    }

    static class Point{
        int x, y;

        public Point(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
}