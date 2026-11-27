# Property source precedence (`property-source-winner`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 709214249153424204, level 2

Spring Boot 4, profile `prod` active: `acme.timeout` is 10 in `application.properties` outside the jar, 60 in `application.yaml` inside the jar, 40 in `application-prod.properties` outside the jar and 25 in `application-prod.properties` inside the jar. Which value wins?

a) `60`
b) `25`
c) `40`
d) `10`

**Key: c**

Explanation: Inputs: `application.properties` outside the jar = 10, `application.yaml` inside the jar = 60, `application-prod.properties` outside the jar = 40, `application-prod.properties` inside the jar = 25. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: `application.yaml` inside the jar (60), then `application-prod.properties` inside the jar (25), then `application.properties` outside the jar (10), then `application-prod.properties` outside the jar (40). Step 2: the last one in that order, `application-prod.properties` outside the jar, overrides all the others. Result: `40`. The other values come from misreadings: `60` from believing that the first source read wins; `25` from believing that a file inside the jar outranks one outside; `10` from believing that the plain file outranks its profile file. Source: `spring-boot-features-external-config#page-title`.

## 2. seed 2457907553949669440, level 1

Spring Boot 4: `acme.timeout` is 40 in the default properties, 10 in environment variable `ACME_TIMEOUT`, 150 in `application.properties` inside the jar and 60 in system property `-Dacme.timeout`. Which value wins?

a) `60`
b) `40`
c) `150`
d) `10`

**Key: a**

Explanation: Inputs: the default properties = 40, environment variable `ACME_TIMEOUT` = 10, `application.properties` inside the jar = 150, system property `-Dacme.timeout` = 60. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (40), then `application.properties` inside the jar (150), then environment variable `ACME_TIMEOUT` (10), then system property `-Dacme.timeout` (60). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `60`. The other values come from misreadings: `40` from believing that the first source read wins; `150` from believing that files outrank the environment and arguments; `10` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 3. seed 1189385236719369749, level 1

Spring Boot 4: `acme.timeout` is 60 in the default properties, 15 in system property `-Dacme.timeout`, 25 in `application.properties` inside the jar and 10 in environment variable `ACME_TIMEOUT`. Which value wins?

a) `15`
b) `25`
c) `60`
d) `10`

**Key: a**

Explanation: Inputs: the default properties = 60, system property `-Dacme.timeout` = 15, `application.properties` inside the jar = 25, environment variable `ACME_TIMEOUT` = 10. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (60), then `application.properties` inside the jar (25), then environment variable `ACME_TIMEOUT` (10), then system property `-Dacme.timeout` (15). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `15`. The other values come from misreadings: `60` from believing that the first source read wins; `25` from believing that files outrank the environment and arguments; `10` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 4. seed 95219409995558817, level 1

Spring Boot 4: `acme.timeout` is 15 in `application.properties` inside the jar, 100 in the default properties, 60 in system property `-Dacme.timeout` and 5 in environment variable `ACME_TIMEOUT`. Which value wins?

a) `100`
b) `5`
c) `60`
d) `15`

**Key: c**

Explanation: Inputs: `application.properties` inside the jar = 15, the default properties = 100, system property `-Dacme.timeout` = 60, environment variable `ACME_TIMEOUT` = 5. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (100), then `application.properties` inside the jar (15), then environment variable `ACME_TIMEOUT` (5), then system property `-Dacme.timeout` (60). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `60`. The other values come from misreadings: `100` from believing that the first source read wins; `15` from believing that files outrank the environment and arguments; `5` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 5. seed 3455058097445701127, level 2

Spring Boot 4, profile `prod` active: `acme.timeout` is 5 in `application.properties` outside the jar, 15 in `application.yaml` inside the jar, 100 in `application-prod.properties` inside the jar and 10 in `application-prod.properties` outside the jar. Which value wins?

a) `100`
b) `15`
c) `5`
d) `10`

**Key: d**

Explanation: Inputs: `application.properties` outside the jar = 5, `application.yaml` inside the jar = 15, `application-prod.properties` inside the jar = 100, `application-prod.properties` outside the jar = 10. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: `application.yaml` inside the jar (15), then `application-prod.properties` inside the jar (100), then `application.properties` outside the jar (5), then `application-prod.properties` outside the jar (10). Step 2: the last one in that order, `application-prod.properties` outside the jar, overrides all the others. Result: `10`. The other values come from misreadings: `15` from believing that the first source read wins; `100` from believing that a file inside the jar outranks one outside; `5` from believing that the plain file outranks its profile file. Source: `spring-boot-features-external-config#page-title`.

## 6. seed 3116197817434484140, level 1

Spring Boot 4: `acme.timeout` is 40 in the default properties, 60 in `application.properties` inside the jar, 5 in system property `-Dacme.timeout` and 10 in environment variable `ACME_TIMEOUT`. Which value wins?

a) `60`
b) `10`
c) `5`
d) `40`

**Key: c**

Explanation: Inputs: the default properties = 40, `application.properties` inside the jar = 60, system property `-Dacme.timeout` = 5, environment variable `ACME_TIMEOUT` = 10. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (40), then `application.properties` inside the jar (60), then environment variable `ACME_TIMEOUT` (10), then system property `-Dacme.timeout` (5). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `5`. The other values come from misreadings: `40` from believing that the first source read wins; `60` from believing that files outrank the environment and arguments; `10` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 7. seed 2659108711856575258, level 1

Spring Boot 4: `acme.timeout` is 60 in `application.properties` inside the jar, 15 in system property `-Dacme.timeout`, 40 in the default properties and 25 in environment variable `ACME_TIMEOUT`. Which value wins?

a) `25`
b) `15`
c) `40`
d) `60`

**Key: b**

Explanation: Inputs: `application.properties` inside the jar = 60, system property `-Dacme.timeout` = 15, the default properties = 40, environment variable `ACME_TIMEOUT` = 25. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (40), then `application.properties` inside the jar (60), then environment variable `ACME_TIMEOUT` (25), then system property `-Dacme.timeout` (15). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `15`. The other values come from misreadings: `40` from believing that the first source read wins; `60` from believing that files outrank the environment and arguments; `25` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 8. seed 3965376640757394155, level 1

Spring Boot 4: `acme.timeout` is 10 in the default properties, 150 in system property `-Dacme.timeout`, 60 in `application.properties` inside the jar and 5 in environment variable `ACME_TIMEOUT`. Which value wins?

a) `10`
b) `150`
c) `5`
d) `60`

**Key: b**

Explanation: Inputs: the default properties = 10, system property `-Dacme.timeout` = 150, `application.properties` inside the jar = 60, environment variable `ACME_TIMEOUT` = 5. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (10), then `application.properties` inside the jar (60), then environment variable `ACME_TIMEOUT` (5), then system property `-Dacme.timeout` (150). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `150`. The other values come from misreadings: `10` from believing that the first source read wins; `60` from believing that files outrank the environment and arguments; `5` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 9. seed 1786145664002517690, level 1

Spring Boot 4: `acme.timeout` is 15 in `application.properties` inside the jar, 60 in system property `-Dacme.timeout`, 5 in environment variable `ACME_TIMEOUT` and 40 in the default properties. Which value wins?

a) `60`
b) `40`
c) `5`
d) `15`

**Key: a**

Explanation: Inputs: `application.properties` inside the jar = 15, system property `-Dacme.timeout` = 60, environment variable `ACME_TIMEOUT` = 5, the default properties = 40. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (40), then `application.properties` inside the jar (15), then environment variable `ACME_TIMEOUT` (5), then system property `-Dacme.timeout` (60). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `60`. The other values come from misreadings: `40` from believing that the first source read wins; `15` from believing that files outrank the environment and arguments; `5` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 10. seed 3618797012116132388, level 1

Spring Boot 4: `acme.timeout` is 60 in system property `-Dacme.timeout`, 5 in the default properties, 40 in `application.properties` inside the jar and 100 in environment variable `ACME_TIMEOUT`. Which value wins?

a) `100`
b) `40`
c) `5`
d) `60`

**Key: d**

Explanation: Inputs: system property `-Dacme.timeout` = 60, the default properties = 5, `application.properties` inside the jar = 40, environment variable `ACME_TIMEOUT` = 100. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (5), then `application.properties` inside the jar (40), then environment variable `ACME_TIMEOUT` (100), then system property `-Dacme.timeout` (60). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `60`. The other values come from misreadings: `5` from believing that the first source read wins; `40` from believing that files outrank the environment and arguments; `100` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 11. seed 1262192332221833216, level 1

Spring Boot 4: `acme.timeout` is 60 in `application.properties` inside the jar, 25 in system property `-Dacme.timeout`, 100 in environment variable `ACME_TIMEOUT` and 40 in the default properties. Which value wins?

a) `60`
b) `25`
c) `100`
d) `40`

**Key: b**

Explanation: Inputs: `application.properties` inside the jar = 60, system property `-Dacme.timeout` = 25, environment variable `ACME_TIMEOUT` = 100, the default properties = 40. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (40), then `application.properties` inside the jar (60), then environment variable `ACME_TIMEOUT` (100), then system property `-Dacme.timeout` (25). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `25`. The other values come from misreadings: `40` from believing that the first source read wins; `60` from believing that files outrank the environment and arguments; `100` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 12. seed 3553314085960449779, level 1

Spring Boot 4: `acme.timeout` is 150 in the default properties, 15 in `application.properties` inside the jar, 100 in system property `-Dacme.timeout` and 25 in environment variable `ACME_TIMEOUT`. Which value wins?

a) `150`
b) `100`
c) `25`
d) `15`

**Key: b**

Explanation: Inputs: the default properties = 150, `application.properties` inside the jar = 15, system property `-Dacme.timeout` = 100, environment variable `ACME_TIMEOUT` = 25. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (150), then `application.properties` inside the jar (15), then environment variable `ACME_TIMEOUT` (25), then system property `-Dacme.timeout` (100). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `100`. The other values come from misreadings: `150` from believing that the first source read wins; `15` from believing that files outrank the environment and arguments; `25` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 13. seed 125842997177507794, level 2

Spring Boot 4: `acme.timeout` is 25 in `application.properties` outside the jar, 15 in system property `-Dacme.timeout`, 40 in `application.properties` inside the jar and 10 in environment variable `ACME_TIMEOUT`. Which value wins?

a) `40`
b) `15`
c) `25`
d) `10`

**Key: b**

Explanation: Inputs: `application.properties` outside the jar = 25, system property `-Dacme.timeout` = 15, `application.properties` inside the jar = 40, environment variable `ACME_TIMEOUT` = 10. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: `application.properties` inside the jar (40), then `application.properties` outside the jar (25), then environment variable `ACME_TIMEOUT` (10), then system property `-Dacme.timeout` (15). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `15`. The other values come from misreadings: `40` from believing that the first source read wins; `25` from believing that files outrank the environment and arguments; `10` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 14. seed 1134626256303732255, level 1

Spring Boot 4: `acme.timeout` is 5 in system property `-Dacme.timeout`, 150 in `application.properties` inside the jar, 100 in environment variable `ACME_TIMEOUT` and 25 in the default properties. Which value wins?

a) `25`
b) `100`
c) `5`
d) `150`

**Key: c**

Explanation: Inputs: system property `-Dacme.timeout` = 5, `application.properties` inside the jar = 150, environment variable `ACME_TIMEOUT` = 100, the default properties = 25. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (25), then `application.properties` inside the jar (150), then environment variable `ACME_TIMEOUT` (100), then system property `-Dacme.timeout` (5). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `5`. The other values come from misreadings: `25` from believing that the first source read wins; `150` from believing that files outrank the environment and arguments; `100` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 15. seed 229906584913290374, level 2

Spring Boot 4, profile `prod` active: `acme.timeout` is 25 in system property `-Dacme.timeout`, 150 in `application.properties` outside the jar, 15 in environment variable `ACME_TIMEOUT` and 5 in `application-prod.properties` inside the jar. Which value wins?

a) `5`
b) `150`
c) `25`
d) `15`

**Key: c**

Explanation: Inputs: system property `-Dacme.timeout` = 25, `application.properties` outside the jar = 150, environment variable `ACME_TIMEOUT` = 15, `application-prod.properties` inside the jar = 5. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: `application-prod.properties` inside the jar (5), then `application.properties` outside the jar (150), then environment variable `ACME_TIMEOUT` (15), then system property `-Dacme.timeout` (25). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `25`. The other values come from misreadings: `5` from believing that the first source read wins; `150` from believing that files outrank the environment and arguments; `15` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 16. seed 182787951976433482, level 1

Spring Boot 4: `acme.timeout` is 5 in environment variable `ACME_TIMEOUT`, 60 in system property `-Dacme.timeout`, 40 in the default properties and 25 in `application.properties` inside the jar. Which value wins?

a) `5`
b) `40`
c) `25`
d) `60`

**Key: d**

Explanation: Inputs: environment variable `ACME_TIMEOUT` = 5, system property `-Dacme.timeout` = 60, the default properties = 40, `application.properties` inside the jar = 25. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (40), then `application.properties` inside the jar (25), then environment variable `ACME_TIMEOUT` (5), then system property `-Dacme.timeout` (60). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `60`. The other values come from misreadings: `40` from believing that the first source read wins; `25` from believing that files outrank the environment and arguments; `5` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 17. seed 819661147626334165, level 2

Spring Boot 4: `acme.timeout` is 40 in environment variable `ACME_TIMEOUT`, 60 in `application.properties` inside the jar, 100 in system property `-Dacme.timeout` and 25 in `application.properties` outside the jar. Which value wins?

a) `40`
b) `60`
c) `100`
d) `25`

**Key: c**

Explanation: Inputs: environment variable `ACME_TIMEOUT` = 40, `application.properties` inside the jar = 60, system property `-Dacme.timeout` = 100, `application.properties` outside the jar = 25. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: `application.properties` inside the jar (60), then `application.properties` outside the jar (25), then environment variable `ACME_TIMEOUT` (40), then system property `-Dacme.timeout` (100). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `100`. The other values come from misreadings: `60` from believing that the first source read wins; `25` from believing that files outrank the environment and arguments; `40` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 18. seed 899971324601693293, level 2

Spring Boot 4: `acme.timeout` is 60 in `application.properties` outside the jar, 150 in `application.yaml` inside the jar, 10 in system property `-Dacme.timeout` and 40 in environment variable `ACME_TIMEOUT`. Which value wins?

a) `150`
b) `40`
c) `60`
d) `10`

**Key: d**

Explanation: Inputs: `application.properties` outside the jar = 60, `application.yaml` inside the jar = 150, system property `-Dacme.timeout` = 10, environment variable `ACME_TIMEOUT` = 40. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: `application.yaml` inside the jar (150), then `application.properties` outside the jar (60), then environment variable `ACME_TIMEOUT` (40), then system property `-Dacme.timeout` (10). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `10`. The other values come from misreadings: `150` from believing that the first source read wins; `60` from believing that files outrank the environment and arguments; `40` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 19. seed 518906306720688424, level 2

Spring Boot 4, profile `prod` active: `acme.timeout` is 15 in the default properties, 10 in `application.properties` outside the jar, 5 in `application-prod.properties` outside the jar and 40 in `application.properties` inside the jar. Which value wins?

a) `5`
b) `40`
c) `10`
d) `15`

**Key: a**

Explanation: Inputs: the default properties = 15, `application.properties` outside the jar = 10, `application-prod.properties` outside the jar = 5, `application.properties` inside the jar = 40. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (15), then `application.properties` inside the jar (40), then `application.properties` outside the jar (10), then `application-prod.properties` outside the jar (5). Step 2: the last one in that order, `application-prod.properties` outside the jar, overrides all the others. Result: `5`. The other values come from misreadings: `15` from believing that the first source read wins; `40` from believing that a file inside the jar outranks one outside; `10` from believing that the plain file outranks its profile file. Source: `spring-boot-features-external-config#page-title`.

## 20. seed 4591241333468475918, level 1

Spring Boot 4: `acme.timeout` is 5 in system property `-Dacme.timeout`, 150 in environment variable `ACME_TIMEOUT`, 40 in `application.properties` inside the jar and 25 in the default properties. Which value wins?

a) `5`
b) `25`
c) `40`
d) `150`

**Key: a**

Explanation: Inputs: system property `-Dacme.timeout` = 5, environment variable `ACME_TIMEOUT` = 150, `application.properties` inside the jar = 40, the default properties = 25. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (25), then `application.properties` inside the jar (40), then environment variable `ACME_TIMEOUT` (150), then system property `-Dacme.timeout` (5). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `5`. The other values come from misreadings: `25` from believing that the first source read wins; `40` from believing that files outrank the environment and arguments; `150` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 21. seed 2523858203295776717, level 2

Spring Boot 4, profile `prod` active: `acme.timeout` is 150 in `application.yaml` inside the jar, 25 in `application.properties` outside the jar, 100 in `application-prod.properties` outside the jar and 60 in the default properties. Which value wins?

a) `150`
b) `25`
c) `100`
d) `60`

**Key: c**

Explanation: Inputs: `application.yaml` inside the jar = 150, `application.properties` outside the jar = 25, `application-prod.properties` outside the jar = 100, the default properties = 60. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (60), then `application.yaml` inside the jar (150), then `application.properties` outside the jar (25), then `application-prod.properties` outside the jar (100). Step 2: the last one in that order, `application-prod.properties` outside the jar, overrides all the others. Result: `100`. The other values come from misreadings: `60` from believing that the first source read wins; `150` from believing that a file inside the jar outranks one outside; `25` from believing that the plain file outranks its profile file. Source: `spring-boot-features-external-config#page-title`.

## 22. seed 3276115360684092885, level 2

Spring Boot 4, profile `prod` active: `acme.timeout` is 15 in `application.properties` inside the jar, 40 in system property `-Dacme.timeout`, 100 in `application-prod.properties` outside the jar and 25 in environment variable `ACME_TIMEOUT`. Which value wins?

a) `100`
b) `40`
c) `15`
d) `25`

**Key: b**

Explanation: Inputs: `application.properties` inside the jar = 15, system property `-Dacme.timeout` = 40, `application-prod.properties` outside the jar = 100, environment variable `ACME_TIMEOUT` = 25. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: `application.properties` inside the jar (15), then `application-prod.properties` outside the jar (100), then environment variable `ACME_TIMEOUT` (25), then system property `-Dacme.timeout` (40). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `40`. The other values come from misreadings: `15` from believing that the first source read wins; `100` from believing that files outrank the environment and arguments; `25` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 23. seed 3405303517159121690, level 1

Spring Boot 4: `acme.timeout` is 5 in the default properties, 60 in system property `-Dacme.timeout`, 40 in `application.properties` inside the jar and 15 in environment variable `ACME_TIMEOUT`. Which value wins?

a) `15`
b) `40`
c) `60`
d) `5`

**Key: c**

Explanation: Inputs: the default properties = 5, system property `-Dacme.timeout` = 60, `application.properties` inside the jar = 40, environment variable `ACME_TIMEOUT` = 15. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (5), then `application.properties` inside the jar (40), then environment variable `ACME_TIMEOUT` (15), then system property `-Dacme.timeout` (60). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `60`. The other values come from misreadings: `5` from believing that the first source read wins; `40` from believing that files outrank the environment and arguments; `15` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 24. seed 1215923988037850383, level 2

Spring Boot 4, profile `prod` active: `acme.timeout` is 10 in `application.properties` outside the jar, 15 in the default properties, 60 in `application-prod.properties` outside the jar and 25 in `application.properties` inside the jar. Which value wins?

a) `60`
b) `25`
c) `15`
d) `10`

**Key: a**

Explanation: Inputs: `application.properties` outside the jar = 10, the default properties = 15, `application-prod.properties` outside the jar = 60, `application.properties` inside the jar = 25. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (15), then `application.properties` inside the jar (25), then `application.properties` outside the jar (10), then `application-prod.properties` outside the jar (60). Step 2: the last one in that order, `application-prod.properties` outside the jar, overrides all the others. Result: `60`. The other values come from misreadings: `15` from believing that the first source read wins; `25` from believing that a file inside the jar outranks one outside; `10` from believing that the plain file outranks its profile file. Source: `spring-boot-features-external-config#page-title`.

## 25. seed 3853440501748138190, level 1

Spring Boot 4: `acme.timeout` is 150 in `application.properties` inside the jar, 15 in the default properties, 25 in environment variable `ACME_TIMEOUT` and 100 in system property `-Dacme.timeout`. Which value wins?

a) `100`
b) `15`
c) `25`
d) `150`

**Key: a**

Explanation: Inputs: `application.properties` inside the jar = 150, the default properties = 15, environment variable `ACME_TIMEOUT` = 25, system property `-Dacme.timeout` = 100. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (15), then `application.properties` inside the jar (150), then environment variable `ACME_TIMEOUT` (25), then system property `-Dacme.timeout` (100). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `100`. The other values come from misreadings: `15` from believing that the first source read wins; `150` from believing that files outrank the environment and arguments; `25` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 26. seed 2458928141480679585, level 1

Spring Boot 4: `acme.timeout` is 60 in system property `-Dacme.timeout`, 40 in the default properties, 10 in `application.properties` inside the jar and 150 in environment variable `ACME_TIMEOUT`. Which value wins?

a) `40`
b) `60`
c) `150`
d) `10`

**Key: b**

Explanation: Inputs: system property `-Dacme.timeout` = 60, the default properties = 40, `application.properties` inside the jar = 10, environment variable `ACME_TIMEOUT` = 150. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (40), then `application.properties` inside the jar (10), then environment variable `ACME_TIMEOUT` (150), then system property `-Dacme.timeout` (60). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `60`. The other values come from misreadings: `40` from believing that the first source read wins; `10` from believing that files outrank the environment and arguments; `150` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 27. seed 715809767185866279, level 2

Spring Boot 4, profile `prod` active: `acme.timeout` is 10 in `application.properties` outside the jar, 60 in `application-prod.properties` outside the jar, 150 in `application.yaml` inside the jar and 100 in the default properties. Which value wins?

a) `150`
b) `10`
c) `100`
d) `60`

**Key: d**

Explanation: Inputs: `application.properties` outside the jar = 10, `application-prod.properties` outside the jar = 60, `application.yaml` inside the jar = 150, the default properties = 100. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (100), then `application.yaml` inside the jar (150), then `application.properties` outside the jar (10), then `application-prod.properties` outside the jar (60). Step 2: the last one in that order, `application-prod.properties` outside the jar, overrides all the others. Result: `60`. The other values come from misreadings: `100` from believing that the first source read wins; `150` from believing that a file inside the jar outranks one outside; `10` from believing that the plain file outranks its profile file. Source: `spring-boot-features-external-config#page-title`.

## 28. seed 4447349692390794254, level 2

Spring Boot 4: `acme.timeout` is 100 in environment variable `ACME_TIMEOUT`, 60 in `application.properties` inside the jar, 40 in system property `-Dacme.timeout` and 150 in `application.properties` outside the jar. Which value wins?

a) `60`
b) `100`
c) `40`
d) `150`

**Key: c**

Explanation: Inputs: environment variable `ACME_TIMEOUT` = 100, `application.properties` inside the jar = 60, system property `-Dacme.timeout` = 40, `application.properties` outside the jar = 150. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: `application.properties` inside the jar (60), then `application.properties` outside the jar (150), then environment variable `ACME_TIMEOUT` (100), then system property `-Dacme.timeout` (40). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `40`. The other values come from misreadings: `60` from believing that the first source read wins; `150` from believing that files outrank the environment and arguments; `100` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 29. seed 3715992129082643489, level 2

Spring Boot 4, profile `prod` active: `acme.timeout` is 100 in `application-prod.properties` outside the jar, 10 in system property `-Dacme.timeout`, 40 in environment variable `ACME_TIMEOUT` and 5 in `application.properties` outside the jar. Which value wins?

a) `40`
b) `10`
c) `5`
d) `100`

**Key: b**

Explanation: Inputs: `application-prod.properties` outside the jar = 100, system property `-Dacme.timeout` = 10, environment variable `ACME_TIMEOUT` = 40, `application.properties` outside the jar = 5. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: `application.properties` outside the jar (5), then `application-prod.properties` outside the jar (100), then environment variable `ACME_TIMEOUT` (40), then system property `-Dacme.timeout` (10). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `10`. The other values come from misreadings: `5` from believing that the first source read wins; `100` from believing that files outrank the environment and arguments; `40` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 30. seed 219984023279904206, level 2

Spring Boot 4: `acme.timeout` is 25 in environment variable `ACME_TIMEOUT`, 40 in `application.properties` inside the jar, 15 in system property `-Dacme.timeout` and 60 in `application.properties` outside the jar. Which value wins?

a) `15`
b) `60`
c) `40`
d) `25`

**Key: a**

Explanation: Inputs: environment variable `ACME_TIMEOUT` = 25, `application.properties` inside the jar = 40, system property `-Dacme.timeout` = 15, `application.properties` outside the jar = 60. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: `application.properties` inside the jar (40), then `application.properties` outside the jar (60), then environment variable `ACME_TIMEOUT` (25), then system property `-Dacme.timeout` (15). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `15`. The other values come from misreadings: `40` from believing that the first source read wins; `60` from believing that files outrank the environment and arguments; `25` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 31. seed 290249723641762453, level 1

Spring Boot 4: `acme.timeout` is 40 in `application.properties` inside the jar, 15 in system property `-Dacme.timeout`, 25 in environment variable `ACME_TIMEOUT` and 60 in the default properties. Which value wins?

a) `60`
b) `15`
c) `25`
d) `40`

**Key: b**

Explanation: Inputs: `application.properties` inside the jar = 40, system property `-Dacme.timeout` = 15, environment variable `ACME_TIMEOUT` = 25, the default properties = 60. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (60), then `application.properties` inside the jar (40), then environment variable `ACME_TIMEOUT` (25), then system property `-Dacme.timeout` (15). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `15`. The other values come from misreadings: `60` from believing that the first source read wins; `40` from believing that files outrank the environment and arguments; `25` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 32. seed 281977589818317682, level 2

Spring Boot 4, profile `prod` active: `acme.timeout` is 25 in `application-prod.properties` outside the jar, 60 in the default properties, 100 in `application.properties` inside the jar and 10 in `application.properties` outside the jar. Which value wins?

a) `60`
b) `25`
c) `10`
d) `100`

**Key: b**

Explanation: Inputs: `application-prod.properties` outside the jar = 25, the default properties = 60, `application.properties` inside the jar = 100, `application.properties` outside the jar = 10. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (60), then `application.properties` inside the jar (100), then `application.properties` outside the jar (10), then `application-prod.properties` outside the jar (25). Step 2: the last one in that order, `application-prod.properties` outside the jar, overrides all the others. Result: `25`. The other values come from misreadings: `60` from believing that the first source read wins; `100` from believing that a file inside the jar outranks one outside; `10` from believing that the plain file outranks its profile file. Source: `spring-boot-features-external-config#page-title`.

## 33. seed 3604399969316534363, level 2

Spring Boot 4, profile `prod` active: `acme.timeout` is 25 in `application-prod.properties` outside the jar, 60 in `application.properties` outside the jar, 15 in `application-prod.properties` inside the jar and 40 in the default properties. Which value wins?

a) `25`
b) `60`
c) `15`
d) `40`

**Key: a**

Explanation: Inputs: `application-prod.properties` outside the jar = 25, `application.properties` outside the jar = 60, `application-prod.properties` inside the jar = 15, the default properties = 40. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (40), then `application-prod.properties` inside the jar (15), then `application.properties` outside the jar (60), then `application-prod.properties` outside the jar (25). Step 2: the last one in that order, `application-prod.properties` outside the jar, overrides all the others. Result: `25`. The other values come from misreadings: `40` from believing that the first source read wins; `15` from believing that a file inside the jar outranks one outside; `60` from believing that the plain file outranks its profile file. Source: `spring-boot-features-external-config#page-title`.

## 34. seed 2177325528928159227, level 1

Spring Boot 4: `acme.timeout` is 40 in environment variable `ACME_TIMEOUT`, 25 in the default properties, 10 in `application.properties` inside the jar and 15 in system property `-Dacme.timeout`. Which value wins?

a) `40`
b) `15`
c) `10`
d) `25`

**Key: b**

Explanation: Inputs: environment variable `ACME_TIMEOUT` = 40, the default properties = 25, `application.properties` inside the jar = 10, system property `-Dacme.timeout` = 15. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (25), then `application.properties` inside the jar (10), then environment variable `ACME_TIMEOUT` (40), then system property `-Dacme.timeout` (15). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `15`. The other values come from misreadings: `25` from believing that the first source read wins; `10` from believing that files outrank the environment and arguments; `40` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 35. seed 4480514610890126196, level 2

Spring Boot 4, profile `prod` active: `acme.timeout` is 100 in environment variable `ACME_TIMEOUT`, 40 in `application.yaml` inside the jar, 5 in system property `-Dacme.timeout` and 10 in `application-prod.properties` inside the jar. Which value wins?

a) `40`
b) `5`
c) `100`
d) `10`

**Key: b**

Explanation: Inputs: environment variable `ACME_TIMEOUT` = 100, `application.yaml` inside the jar = 40, system property `-Dacme.timeout` = 5, `application-prod.properties` inside the jar = 10. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: `application.yaml` inside the jar (40), then `application-prod.properties` inside the jar (10), then environment variable `ACME_TIMEOUT` (100), then system property `-Dacme.timeout` (5). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `5`. The other values come from misreadings: `40` from believing that the first source read wins; `10` from believing that files outrank the environment and arguments; `100` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 36. seed 2056776668811212535, level 1

Spring Boot 4: `acme.timeout` is 10 in system property `-Dacme.timeout`, 25 in the default properties, 15 in environment variable `ACME_TIMEOUT` and 60 in `application.properties` inside the jar. Which value wins?

a) `10`
b) `15`
c) `60`
d) `25`

**Key: a**

Explanation: Inputs: system property `-Dacme.timeout` = 10, the default properties = 25, environment variable `ACME_TIMEOUT` = 15, `application.properties` inside the jar = 60. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (25), then `application.properties` inside the jar (60), then environment variable `ACME_TIMEOUT` (15), then system property `-Dacme.timeout` (10). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `10`. The other values come from misreadings: `25` from believing that the first source read wins; `60` from believing that files outrank the environment and arguments; `15` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 37. seed 622830463648662051, level 1

Spring Boot 4: `acme.timeout` is 150 in the default properties, 100 in system property `-Dacme.timeout`, 60 in environment variable `ACME_TIMEOUT` and 25 in `application.properties` inside the jar. Which value wins?

a) `100`
b) `150`
c) `25`
d) `60`

**Key: a**

Explanation: Inputs: the default properties = 150, system property `-Dacme.timeout` = 100, environment variable `ACME_TIMEOUT` = 60, `application.properties` inside the jar = 25. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (150), then `application.properties` inside the jar (25), then environment variable `ACME_TIMEOUT` (60), then system property `-Dacme.timeout` (100). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `100`. The other values come from misreadings: `150` from believing that the first source read wins; `25` from believing that files outrank the environment and arguments; `60` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 38. seed 3026731005830936683, level 2

Spring Boot 4, profile `prod` active: `acme.timeout` is 25 in `application-prod.properties` outside the jar, 10 in `application-prod.properties` inside the jar, 15 in the default properties and 40 in `application.properties` outside the jar. Which value wins?

a) `25`
b) `15`
c) `10`
d) `40`

**Key: a**

Explanation: Inputs: `application-prod.properties` outside the jar = 25, `application-prod.properties` inside the jar = 10, the default properties = 15, `application.properties` outside the jar = 40. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (15), then `application-prod.properties` inside the jar (10), then `application.properties` outside the jar (40), then `application-prod.properties` outside the jar (25). Step 2: the last one in that order, `application-prod.properties` outside the jar, overrides all the others. Result: `25`. The other values come from misreadings: `15` from believing that the first source read wins; `10` from believing that a file inside the jar outranks one outside; `40` from believing that the plain file outranks its profile file. Source: `spring-boot-features-external-config#page-title`.

## 39. seed 1561217701187619592, level 2

Spring Boot 4: `acme.timeout` is 150 in environment variable `ACME_TIMEOUT`, 60 in `application.properties` inside the jar, 100 in `application.properties` outside the jar and 40 in system property `-Dacme.timeout`. Which value wins?

a) `100`
b) `60`
c) `150`
d) `40`

**Key: d**

Explanation: Inputs: environment variable `ACME_TIMEOUT` = 150, `application.properties` inside the jar = 60, `application.properties` outside the jar = 100, system property `-Dacme.timeout` = 40. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: `application.properties` inside the jar (60), then `application.properties` outside the jar (100), then environment variable `ACME_TIMEOUT` (150), then system property `-Dacme.timeout` (40). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `40`. The other values come from misreadings: `60` from believing that the first source read wins; `100` from believing that files outrank the environment and arguments; `150` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 40. seed 829843593659301200, level 2

Spring Boot 4: `acme.timeout` is 15 in environment variable `ACME_TIMEOUT`, 5 in `application.properties` outside the jar, 40 in system property `-Dacme.timeout` and 25 in `application.yaml` inside the jar. Which value wins?

a) `5`
b) `25`
c) `15`
d) `40`

**Key: d**

Explanation: Inputs: environment variable `ACME_TIMEOUT` = 15, `application.properties` outside the jar = 5, system property `-Dacme.timeout` = 40, `application.yaml` inside the jar = 25. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: `application.yaml` inside the jar (25), then `application.properties` outside the jar (5), then environment variable `ACME_TIMEOUT` (15), then system property `-Dacme.timeout` (40). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `40`. The other values come from misreadings: `25` from believing that the first source read wins; `5` from believing that files outrank the environment and arguments; `15` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 41. seed 1575251710864550405, level 1

Spring Boot 4: `acme.timeout` is 40 in `application.properties` inside the jar, 60 in system property `-Dacme.timeout`, 15 in environment variable `ACME_TIMEOUT` and 10 in the default properties. Which value wins?

a) `60`
b) `15`
c) `10`
d) `40`

**Key: a**

Explanation: Inputs: `application.properties` inside the jar = 40, system property `-Dacme.timeout` = 60, environment variable `ACME_TIMEOUT` = 15, the default properties = 10. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (10), then `application.properties` inside the jar (40), then environment variable `ACME_TIMEOUT` (15), then system property `-Dacme.timeout` (60). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `60`. The other values come from misreadings: `10` from believing that the first source read wins; `40` from believing that files outrank the environment and arguments; `15` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 42. seed 4146051485560145415, level 2

Spring Boot 4, profile `prod` active: `acme.timeout` is 10 in system property `-Dacme.timeout`, 25 in environment variable `ACME_TIMEOUT`, 40 in `application-prod.properties` inside the jar and 5 in `application.properties` outside the jar. Which value wins?

a) `5`
b) `40`
c) `25`
d) `10`

**Key: d**

Explanation: Inputs: system property `-Dacme.timeout` = 10, environment variable `ACME_TIMEOUT` = 25, `application-prod.properties` inside the jar = 40, `application.properties` outside the jar = 5. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: `application-prod.properties` inside the jar (40), then `application.properties` outside the jar (5), then environment variable `ACME_TIMEOUT` (25), then system property `-Dacme.timeout` (10). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `10`. The other values come from misreadings: `40` from believing that the first source read wins; `5` from believing that files outrank the environment and arguments; `25` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 43. seed 3215966504489536492, level 2

Spring Boot 4: `acme.timeout` is 100 in `application.properties` outside the jar, 60 in `application.properties` inside the jar, 150 in environment variable `ACME_TIMEOUT` and 10 in system property `-Dacme.timeout`. Which value wins?

a) `100`
b) `10`
c) `60`
d) `150`

**Key: b**

Explanation: Inputs: `application.properties` outside the jar = 100, `application.properties` inside the jar = 60, environment variable `ACME_TIMEOUT` = 150, system property `-Dacme.timeout` = 10. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: `application.properties` inside the jar (60), then `application.properties` outside the jar (100), then environment variable `ACME_TIMEOUT` (150), then system property `-Dacme.timeout` (10). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `10`. The other values come from misreadings: `60` from believing that the first source read wins; `100` from believing that files outrank the environment and arguments; `150` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 44. seed 4053889386673857146, level 2

Spring Boot 4, profile `prod` active: `acme.timeout` is 40 in `application-prod.properties` outside the jar, 25 in the default properties, 15 in `application.yaml` inside the jar and 10 in `application.properties` outside the jar. Which value wins?

a) `40`
b) `10`
c) `15`
d) `25`

**Key: a**

Explanation: Inputs: `application-prod.properties` outside the jar = 40, the default properties = 25, `application.yaml` inside the jar = 15, `application.properties` outside the jar = 10. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (25), then `application.yaml` inside the jar (15), then `application.properties` outside the jar (10), then `application-prod.properties` outside the jar (40). Step 2: the last one in that order, `application-prod.properties` outside the jar, overrides all the others. Result: `40`. The other values come from misreadings: `25` from believing that the first source read wins; `15` from believing that a file inside the jar outranks one outside; `10` from believing that the plain file outranks its profile file. Source: `spring-boot-features-external-config#page-title`.

## 45. seed 454104535760766525, level 1

Spring Boot 4: `acme.timeout` is 40 in the default properties, 60 in system property `-Dacme.timeout`, 5 in `application.properties` inside the jar and 150 in environment variable `ACME_TIMEOUT`. Which value wins?

a) `60`
b) `5`
c) `40`
d) `150`

**Key: a**

Explanation: Inputs: the default properties = 40, system property `-Dacme.timeout` = 60, `application.properties` inside the jar = 5, environment variable `ACME_TIMEOUT` = 150. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (40), then `application.properties` inside the jar (5), then environment variable `ACME_TIMEOUT` (150), then system property `-Dacme.timeout` (60). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `60`. The other values come from misreadings: `40` from believing that the first source read wins; `5` from believing that files outrank the environment and arguments; `150` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 46. seed 1721093532498862027, level 1

Spring Boot 4: `acme.timeout` is 40 in system property `-Dacme.timeout`, 10 in `application.properties` inside the jar, 60 in environment variable `ACME_TIMEOUT` and 25 in the default properties. Which value wins?

a) `60`
b) `25`
c) `40`
d) `10`

**Key: c**

Explanation: Inputs: system property `-Dacme.timeout` = 40, `application.properties` inside the jar = 10, environment variable `ACME_TIMEOUT` = 60, the default properties = 25. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (25), then `application.properties` inside the jar (10), then environment variable `ACME_TIMEOUT` (60), then system property `-Dacme.timeout` (40). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `40`. The other values come from misreadings: `25` from believing that the first source read wins; `10` from believing that files outrank the environment and arguments; `60` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 47. seed 3816559332701182109, level 1

Spring Boot 4: `acme.timeout` is 15 in `application.properties` inside the jar, 150 in environment variable `ACME_TIMEOUT`, 25 in the default properties and 100 in system property `-Dacme.timeout`. Which value wins?

a) `100`
b) `150`
c) `15`
d) `25`

**Key: a**

Explanation: Inputs: `application.properties` inside the jar = 15, environment variable `ACME_TIMEOUT` = 150, the default properties = 25, system property `-Dacme.timeout` = 100. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (25), then `application.properties` inside the jar (15), then environment variable `ACME_TIMEOUT` (150), then system property `-Dacme.timeout` (100). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `100`. The other values come from misreadings: `25` from believing that the first source read wins; `15` from believing that files outrank the environment and arguments; `150` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 48. seed 4078417492302624594, level 2

Spring Boot 4, profile `prod` active: `acme.timeout` is 10 in `application-prod.properties` outside the jar, 150 in `application.properties` inside the jar, 100 in the default properties and 15 in `application.properties` outside the jar. Which value wins?

a) `10`
b) `15`
c) `150`
d) `100`

**Key: a**

Explanation: Inputs: `application-prod.properties` outside the jar = 10, `application.properties` inside the jar = 150, the default properties = 100, `application.properties` outside the jar = 15. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (100), then `application.properties` inside the jar (150), then `application.properties` outside the jar (15), then `application-prod.properties` outside the jar (10). Step 2: the last one in that order, `application-prod.properties` outside the jar, overrides all the others. Result: `10`. The other values come from misreadings: `100` from believing that the first source read wins; `150` from believing that a file inside the jar outranks one outside; `15` from believing that the plain file outranks its profile file. Source: `spring-boot-features-external-config#page-title`.

## 49. seed 1561641109879086520, level 2

Spring Boot 4: `acme.timeout` is 40 in `application.properties` inside the jar, 25 in `application.properties` outside the jar, 150 in system property `-Dacme.timeout` and 15 in environment variable `ACME_TIMEOUT`. Which value wins?

a) `150`
b) `25`
c) `15`
d) `40`

**Key: a**

Explanation: Inputs: `application.properties` inside the jar = 40, `application.properties` outside the jar = 25, system property `-Dacme.timeout` = 150, environment variable `ACME_TIMEOUT` = 15. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: `application.properties` inside the jar (40), then `application.properties` outside the jar (25), then environment variable `ACME_TIMEOUT` (15), then system property `-Dacme.timeout` (150). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `150`. The other values come from misreadings: `40` from believing that the first source read wins; `25` from believing that files outrank the environment and arguments; `15` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.

## 50. seed 102263863204481336, level 1

Spring Boot 4: `acme.timeout` is 25 in `application.properties` inside the jar, 10 in system property `-Dacme.timeout`, 100 in the default properties and 60 in environment variable `ACME_TIMEOUT`. Which value wins?

a) `10`
b) `60`
c) `25`
d) `100`

**Key: a**

Explanation: Inputs: `application.properties` inside the jar = 25, system property `-Dacme.timeout` = 10, the default properties = 100, environment variable `ACME_TIMEOUT` = 60. Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier one; from lowest to highest the sources here rank default properties, application files (YAML before properties, inside the jar before outside, the plain file before its profile file), environment variables, system properties, command-line arguments. Step 1: order the defined sources from the lowest rank: the default properties (100), then `application.properties` inside the jar (25), then environment variable `ACME_TIMEOUT` (60), then system property `-Dacme.timeout` (10). Step 2: the last one in that order, system property `-Dacme.timeout`, overrides all the others. Result: `10`. The other values come from misreadings: `100` from believing that the first source read wins; `25` from believing that files outrank the environment and arguments; `60` from believing that the environment outranks system properties. Source: `spring-boot-features-external-config#page-title`.
