import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static LinkedList<Integer> queue = new LinkedList<>();
    static int[][] data;
    static boolean[][] visited;
    static int[] dx = {-1,1,0,0,-1,1,-1,1};
    static int[] dy = {0,0,-1,1,1,-1,-1,1};
    static int w = 0;
    static int h = 0;
    static int count;


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while(true){
            String[] strings = br.readLine().split(" ");
            w = Integer.parseInt(strings[0]);
            h = Integer.parseInt(strings[1]);


            if(w == 0 && h == 0){
                break;
            } else {
                count = 0;
                data = new int[h][w];
                visited = new boolean[h][w];

                for(int i = 0; i<h; i++){

                    String[] inputs = br.readLine().split(" ");
                    for(int j = 0; j<w; j++){
                        data[i][j] = Integer.parseInt(inputs[j]);
                    }
                }

                for(int i = 0; i<h; i++){
                    for(int j = 0; j<w; j++){
                        if(data[i][j] == 1 && !visited[i][j]){
                            bfs(i,j);
                            count++;
                        }
                    }
                }
                System.out.println(count);
            }
        }
        br.close();
    }

    private static void bfs(int x, int y){
        visited[x][y] = true;
        queue.add(x);
        queue.add(y);

        while(!queue.isEmpty()){
            int qx = queue.poll();
            int qy = queue.poll();

            for(int i = 0; i<8; i++){
                int nx = qx + dx[i];
                int ny = qy + dy[i];

                if(0<=nx && nx<h && 0<=ny && ny<w){
                    if(!visited[nx][ny] && data[nx][ny] == 1){
                        visited[nx][ny] = true;
                        queue.add(nx);
                        queue.add(ny);
                    }
                }
            }
        }
    }
}
