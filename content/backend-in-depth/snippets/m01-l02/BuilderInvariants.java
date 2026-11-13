public class BuilderInvariants {
    static final class Invoice {
        private final String number;
        private final long cents;

        private Invoice(Builder builder) {
            this.number = builder.number;
            this.cents = builder.cents;
        }

        static Builder builder() {
            return new Builder();
        }

        @Override
        public String toString() {
            return "Invoice " + number + " " + cents;
        }

        static final class Builder {
            private String number;
            private long cents = -1;

            Builder number(String number) {
                this.number = number;
                return this;
            }

            Builder cents(long cents) {
                this.cents = cents;
                return this;
            }

            Invoice build() {
                if (number == null || number.isBlank()) {
                    throw new IllegalStateException("number is required");
                }
                if (cents < 0) {
                    throw new IllegalStateException("cents must not be negative");
                }
                return new Invoice(this);
            }
        }
    }

    public static void main(String[] args) {
        System.out.println(Invoice.builder().number("F-1").cents(1200).build());
        try {
            Invoice.builder().number("F-2").build();
        } catch (IllegalStateException e) {
            System.out.println(e.getMessage());
        }
    }
}
