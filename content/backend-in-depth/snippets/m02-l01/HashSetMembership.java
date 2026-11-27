import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

public class HashSetMembership {
    static class Account {
        int id;

        Account(int id) {
            this.id = id;
        }

        @Override
        public boolean equals(Object other) {
            return other instanceof Account that && that.id == id;
        }

        @Override
        public int hashCode() {
            return Objects.hash(id);
        }
    }

    public static void main(String[] args) {
        Set<Account> accounts = new HashSet<>();
        Account account = new Account(7);
        System.out.println("add: " + accounts.add(account));
        System.out.println("add equal copy: " + accounts.add(new Account(7)));
        System.out.println("size: " + accounts.size());

        account.id = 8;
        System.out.println("contains after id change: " + accounts.contains(account));
        System.out.println("size after id change: " + accounts.size());
        System.out.println("found by iteration: " + accounts.stream().anyMatch(held -> held == account));
    }
}
