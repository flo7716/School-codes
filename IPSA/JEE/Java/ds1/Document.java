package ds1;

import java.util.Date;

public class Document {
    private String code;
    private String discipline;
    private String theme;
    private String type;
    private Date date_edition;
    private String langue;
    private int nombre_exemplaires;
    private int nbex_disponibles;
    public Document(String code, String discipline, String theme, String type, Date date_edition, String langue,
            int nombre_exemplaires, int nbex_disponibles) {
        this.code = code;
        this.discipline = discipline;
        this.theme = theme;
        this.type = type;
        this.date_edition = date_edition;
        this.langue = langue;
        this.nombre_exemplaires = nombre_exemplaires;
        this.nbex_disponibles = nbex_disponibles;
    }
    public String getCode() {
        return code;
    }
    public void setCode(String code) {
        this.code = code;
    }
    public String getDiscipline() {
        return discipline;
    }
    public void setDiscipline(String discipline) {
        this.discipline = discipline;
    }
    public String getTheme() {
        return theme;
    }
    public void setTheme(String theme) {
        this.theme = theme;
    }
    public String getType() {
        return type;
    }
    public void setType(String type) {
        this.type = type;
    }
    public Date getDate_edition() {
        return date_edition;
    }
    public void setDate_edition(Date date_edition) {
        this.date_edition = date_edition;
    }
    public String getLangue() {
        return langue;
    }
    public void setLangue(String langue) {
        this.langue = langue;
    }
    public int getNombre_exemplaires() {
        return nombre_exemplaires;
    }
    public void setNombre_exemplaires(int nombre_exemplaires) {
        this.nombre_exemplaires = nombre_exemplaires;
    }
    public int getNbex_disponibles() {
        return nbex_disponibles;
    }
    public void setNbex_disponibles(int nbex_disponibles) {
        this.nbex_disponibles = nbex_disponibles;
    }

    



    

    

    
}
