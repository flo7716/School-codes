public class Table {
    private structure structure;
    private data data;
    public Table(structure structure, data data) {
        this.structure = structure;
        this.data = data;
    }
    public structure getStructure() {
        return structure;
    }
    public void setStructure(structure structure) {
        this.structure = structure;
    }
    public data getData() {
        return data;
    }
    public void setData(data data) {
        this.data = data;
    }

    
}
