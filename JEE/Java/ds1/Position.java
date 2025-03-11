package ds1;
public class Position{
    private float x,y;


    public Position(float x, float y) {
        this.x = x;
        this.y = y;
    }

    

    public float getX() {
        return x;
    }



    public void setX(float x) {
        this.x = x;
    }



    public float getY() {
        return y;
    }



    public void setY(float y) {
        this.y = y;
    }



    @Override
    public String toString() {
        return "Position [x=" + x + ", y=" + y + "]";
    }

    

    
}
