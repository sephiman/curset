public class HashSlot {
    static int crc16(byte[] data) {
        int crc = 0;
        for (byte b : data) {
            crc ^= (b & 0xFF) << 8;
            for (int bit = 0; bit < 8; bit++) {
                crc = (crc & 0x8000) != 0 ? (crc << 1) ^ 0x1021 : crc << 1;
                crc &= 0xFFFF;
            }
        }
        return crc;
    }

    static String hashedPart(String key) {
        int open = key.indexOf('{');
        if (open < 0) {
            return key;
        }
        int close = key.indexOf('}', open + 1);
        if (close < 0 || close == open + 1) {
            return key;
        }
        return key.substring(open + 1, close);
    }

    static int slot(String key) {
        return crc16(hashedPart(key).getBytes(java.nio.charset.StandardCharsets.UTF_8)) % 16384;
    }

    public static void main(String[] args) {
        System.out.println("crc16 of 123456789: " + Integer.toHexString(crc16("123456789".getBytes(java.nio.charset.StandardCharsets.UTF_8))).toUpperCase());
        System.out.println("slot of 123456789: " + slot("123456789"));
        System.out.println("{user1000}.following and {user1000}.followers share a slot: " + (slot("{user1000}.following") == slot("{user1000}.followers")));
        System.out.println("foo{}{bar} is hashed as a whole key: " + (slot("foo{}{bar}") != slot("bar")));
        System.out.println("foo{{bar}}zap hashes {bar: " + (slot("foo{{bar}}zap") == slot("{bar")));
        System.out.println("foo{bar}{zap} hashes bar: " + (slot("foo{bar}{zap}") == slot("bar")));
    }
}
