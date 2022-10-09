import java.io.*;
import java.util.*;

public class Main {

    static StringTokenizer st;

    static int n, m, x, y, nx, ny;
    static int[][] data;
    static int[] dx = {-2, -2, -1, -1, 1, 1, 2, 2};
    static int[] dy = {-1, 1, -2, 2, -2, 2, -1, 1};

    public static void main(String[] args) throws IOException{

        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        data = new int[n + 1][n + 1];
        for(int i = 0; i < n + 1; i++) {
            Arrays.fill(data[i], -1);
        }

        st = new StringTokenizer(br.readLine());
        x = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());

        data[x][y] = 0;


        bfs();

        for(int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());

            sb.append(data[Integer.parseInt(st.nextToken())][Integer.parseInt(st.nextToken())]).append(" ");

        }

        System.out.println(sb);


    }


    public static void bfs(){
        Queue<Point> queue = new LinkedList<>();
        queue.add(new Point(x, y));


        while(!queue.isEmpty()){

            Point point = queue.poll();
            int x = point.x;
            int y = point.y;


            for(int i = 0; i<8; i++) {
                nx = x + dx[i];
                ny = y + dy[i];


                if (0 < nx && nx <= n && 0 < ny && ny <= n) {

                    if (data[nx][ny] == -1) {

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