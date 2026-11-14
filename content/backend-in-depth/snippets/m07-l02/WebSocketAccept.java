import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;
import java.util.HexFormat;

public class WebSocketAccept {
    static final String GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11";

    public static void main(String[] args) throws NoSuchAlgorithmException {
        String key = "dGhlIHNhbXBsZSBub25jZQ==";
        byte[] hash = MessageDigest.getInstance("SHA-1").digest((key + GUID).getBytes(StandardCharsets.US_ASCII));
        System.out.println(HexFormat.of().formatHex(hash));
        System.out.println(Base64.getEncoder().encodeToString(hash).equals("s3pPLMBiTxaQ9kYGzzhZRbK+xOo="));
    }
}
