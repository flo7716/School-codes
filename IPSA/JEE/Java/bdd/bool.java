public class bool extends Type{
    private boolean bool;
    public bool(String nom, boolean bool) {
        super(nom);
        this.bool = bool;
    }
    public boolean getBool() {
        return bool;
    }
    public void setBool(boolean bool) {
        this.bool = bool;
    }
    
}
