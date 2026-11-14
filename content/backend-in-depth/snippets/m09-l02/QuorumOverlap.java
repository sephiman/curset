public class QuorumOverlap {
    record Setting(int replicas, int readQuorum, int writeQuorum) {
        boolean overlaps() {
            return readQuorum + writeQuorum > replicas;
        }
    }

    public static void main(String[] args) {
        Setting[] settings = {
            new Setting(3, 2, 2),
            new Setting(3, 1, 1),
            new Setting(3, 1, 3),
            new Setting(3, 2, 1),
            new Setting(5, 3, 3),
            new Setting(5, 2, 2),
        };
        for (Setting s : settings) {
            System.out.println("N=" + s.replicas() + " R=" + s.readQuorum() + " W=" + s.writeQuorum()
                    + " R+W=" + (s.readQuorum() + s.writeQuorum()) + " overlap=" + s.overlaps());
        }
    }
}
