import java.io.*;
import java.util.*;

public class Main {
    static StringTokenizer st;
    static int n, m, tmp, x, y, nx, ny, cnt = 0, result = 0;
    static int[][] data;
    static Queue<Point> queue = new LinkedList<>();
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        data = new int[n][m];
        for(int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());

            for(int j = 0; j < m; j++){
                tmp = Integer.parseInt(st.nextToken());
                if(tmp == 2){
                    queue.add(new Point(i, j));
                }
                data[i][j] = tmp;
            }
        }

        backTracking(0, 0);
        System.out.println(result);
    }

    public static void backTracking(int startX, int startY){
        if(cnt == 3){

//            System.out.println("before");
//            for(int i = 0; i < n; i++){
//                for(int j = 0; j < m; j++){
//                    System.out.print(data[i][j] + " ");
//                }
//                System.out.println();
//            }
            bfs();

        }else{

            for(int i = startX; i < n; i++){
                for(int j = startY; j < m; j++){
                    if(data[i][j] == 0 && cnt < 3) {

                        cnt++;
                        data[i][j] = 1;
                        backTracking(startX, startY);
                        cnt--;
                        data[i][j] = 0;
                    }
                }
            }
        }
    }

    public static void bfs(){

        int[][] tmpData = new int[n][m];
        for(int i = 0; i <n; i++){
            tmpData[i] = data[i].clone();
        }

        Queue<Point> copiedQueue = new LinkedList<>(queue);

        while(!copiedQueue.isEmpty()) {
            Point point = copiedQueue.poll();
            x = point.x;
            y = point.y;

            for(int i = 0; i < 4; i++){
                nx = x + dx[i];
                ny = y + dy[i];

                if( 0 <= nx && nx < n && 0 <= ny && ny < m ){
                    if(tmpData[nx][ny] == 0){
                        tmpData[nx][ny] = 2;
                        copiedQueue.add(new Point(nx, ny));
                    }
                }
            }
        }

//        System.out.println("after");
        int safeZoneCnt = 0;

        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
//                System.out.print(tmpData[i][j] + " ");
                if(tmpData[i][j] == 0){
                    safeZoneCnt++;
                }
            }
//            System.out.println();
        }
        result = Math.max(safeZoneCnt, result);
    }

    static class Point{
        int x, y;

        public Point(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
}