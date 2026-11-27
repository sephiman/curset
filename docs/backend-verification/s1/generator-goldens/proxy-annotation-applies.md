# Proxy-based advice (`proxy-annotation-applies`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 1169646540074537056, level 2

A method is annotated `@Transactional`. In Spring Framework 7, with a class-based proxy, another bean calls a package-visible method. Does the advice of the annotation run for this call?

a) No: only methods declared on an interface are advised, whatever the visibility is
b) No: a class-based proxy can never override a package-visible method of its target
c) Yes: a class-based proxy advises package-visible methods since Spring Framework 6
d) No: advice applies only to `public` methods, whatever the type of proxy is in use

**Key: c**

Explanation: Inputs: `@Transactional`, call shape: package-private. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy. Step 2: the method is package-visible, which a class-based proxy can advise since 6.0. Result: Yes: a class-based proxy advises package-visible methods since Spring Framework 6. The other options are misreadings: no: advice applies only to `public` methods, whatever the type of proxy is in use; no: a class-based proxy can never override a package-visible method of its target; no: only methods declared on an interface are advised, whatever the visibility is. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 2. seed 4163204911152118082, level 1

A method is annotated `@Cacheable`. In proxy mode, another public method of the bean calls it through a self reference. Does the advice of the annotation run for this call?

a) No: a call from inside the bean always runs on `this` and never reaches the proxy
b) No: the proxy advises a method only if the caller bean carries the annotation too
c) Yes: the call goes through the injected proxy, not through `this`, so advice runs
d) No: a bean cannot hold a reference to its own proxy, so the advice is always lost

**Key: c**

Explanation: Inputs: `@Cacheable`, call shape: self-injection. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy held in the self reference. Step 2: the method is public, so the proxy can advise it. Result: Yes: the call goes through the injected proxy, not through `this`, so advice runs. The other options are misreadings: no: a call from inside the bean always runs on `this` and never reaches the proxy; no: a bean cannot hold a reference to its own proxy, so the advice is always lost; no: the proxy advises a method only if the caller bean carries the annotation too. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 3. seed 4273784624568229157, level 1

A method is annotated `@Async`. In proxy mode, another public method of the bean calls it through a self reference. Does the advice of the annotation run for this call?

a) No: a bean cannot hold a reference to its own proxy, so the advice is always lost
b) No: a call from inside the bean always runs on `this` and never reaches the proxy
c) No: the proxy advises a method only if the caller bean carries the annotation too
d) Yes: the call goes through the injected proxy, not through `this`, so advice runs

**Key: d**

Explanation: Inputs: `@Async`, call shape: self-injection. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy held in the self reference. Step 2: the method is public, so the proxy can advise it. Result: Yes: the call goes through the injected proxy, not through `this`, so advice runs. The other options are misreadings: no: a call from inside the bean always runs on `this` and never reaches the proxy; no: a bean cannot hold a reference to its own proxy, so the advice is always lost; no: the proxy advises a method only if the caller bean carries the annotation too. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 4. seed 1406409125281070917, level 1

A method is annotated `@Async`. In proxy mode, another public method of the same bean calls it as `this.method()`. Does the advice of the annotation run for this call?

a) No: a call on `this` bypasses the proxy, so the interceptor chain does not run it
b) Yes: Spring Boot proxies all of its beans, so every call to any method is advised
c) Yes: the annotation is on that method, and its presence alone triggers the advice
d) Yes: `this` is the proxy inside the bean, so the call is intercepted all the same

**Key: a**

Explanation: Inputs: `@Async`, call shape: self-invocation. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call runs on `this`, inside the target object, and never reaches the proxy. Step 2: the call bypassed the proxy, so the method's visibility does not matter. Result: No: a call on `this` bypasses the proxy, so the interceptor chain does not run it. The other options are misreadings: yes: the annotation is on that method, and its presence alone triggers the advice; yes: spring boot proxies all of its beans, so every call to any method is advised; yes: `this` is the proxy inside the bean, so the call is intercepted all the same. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 5. seed 1767766473155246332, level 1

A method is annotated `@Cacheable`. In proxy mode, another bean calls the public method through its injected reference. Does the advice of the annotation run for this call?

a) No: advice runs only for calls made from inside the same bean, never from another
b) No: the injected reference is the raw target object, and the call skips the proxy
c) Yes: the call comes in through the proxy, which then runs its interceptors for it
d) No: the proxy advises a method only when the calling bean also has the annotation

**Key: c**

Explanation: Inputs: `@Cacheable`, call shape: external. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy. Step 2: the method is public, so the proxy can advise it. Result: Yes: the call comes in through the proxy, which then runs its interceptors for it. The other options are misreadings: no: the injected reference is the raw target object, and the call skips the proxy; no: the proxy advises a method only when the calling bean also has the annotation; no: advice runs only for calls made from inside the same bean, never from another. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 6. seed 2946194546613079819, level 2

A method is annotated `@Cacheable`. In proxy mode, the class has no interface and another bean calls its public `final` method. Does the advice of the annotation run for this call?

a) Yes: the annotation is on that method, and its presence alone triggers the advice
b) Yes: the call comes in through the proxy, hence the interceptor chain runs for it
c) Yes: Spring Boot proxies all of its beans, so every call to any method is advised
d) No: a class-based proxy extends the class and so cannot override a `final` method

**Key: d**

Explanation: Inputs: `@Cacheable`, call shape: final. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy. Step 2: the method is `final`, so a class-based proxy cannot override or advise it. Result: No: a class-based proxy extends the class and so cannot override a `final` method. The other options are misreadings: yes: the annotation is on that method, and its presence alone triggers the advice; yes: spring boot proxies all of its beans, so every call to any method is advised; yes: the call comes in through the proxy, hence the interceptor chain runs for it. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 7. seed 73017781623168965, level 2

A method is annotated `@Transactional`. In proxy mode, another bean calls the public method through its injected reference. Does the advice of the annotation run for this call?

a) No: the proxy advises a method only when the calling bean also has the annotation
b) No: advice runs only for calls made from inside the same bean, never from another
c) Yes: the call comes in through the proxy, which then runs its interceptors for it
d) No: the injected reference is the raw target object, and the call skips the proxy

**Key: c**

Explanation: Inputs: `@Transactional`, call shape: external. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy. Step 2: the method is public, so the proxy can advise it. Result: Yes: the call comes in through the proxy, which then runs its interceptors for it. The other options are misreadings: no: the injected reference is the raw target object, and the call skips the proxy; no: the proxy advises a method only when the calling bean also has the annotation; no: advice runs only for calls made from inside the same bean, never from another. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 8. seed 3938197095525139794, level 1

A method is annotated `@Transactional`. In proxy mode, another bean calls the public method through its injected reference. Does the advice of the annotation run for this call?

a) No: advice runs only for calls made from inside the same bean, never from another
b) No: the proxy advises a method only when the calling bean also has the annotation
c) No: the injected reference is the raw target object, and the call skips the proxy
d) Yes: the call comes in through the proxy, which then runs its interceptors for it

**Key: d**

Explanation: Inputs: `@Transactional`, call shape: external. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy. Step 2: the method is public, so the proxy can advise it. Result: Yes: the call comes in through the proxy, which then runs its interceptors for it. The other options are misreadings: no: the injected reference is the raw target object, and the call skips the proxy; no: the proxy advises a method only when the calling bean also has the annotation; no: advice runs only for calls made from inside the same bean, never from another. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 9. seed 807082757401492745, level 2

A method is annotated `@Transactional`. In Spring Framework 7, with a class-based proxy, another bean calls a package-visible method. Does the advice of the annotation run for this call?

a) No: a class-based proxy can never override a package-visible method of its target
b) No: only methods declared on an interface are advised, whatever the visibility is
c) Yes: a class-based proxy advises package-visible methods since Spring Framework 6
d) No: advice applies only to `public` methods, whatever the type of proxy is in use

**Key: c**

Explanation: Inputs: `@Transactional`, call shape: package-private. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy. Step 2: the method is package-visible, which a class-based proxy can advise since 6.0. Result: Yes: a class-based proxy advises package-visible methods since Spring Framework 6. The other options are misreadings: no: advice applies only to `public` methods, whatever the type of proxy is in use; no: a class-based proxy can never override a package-visible method of its target; no: only methods declared on an interface are advised, whatever the visibility is. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 10. seed 2762181778787690164, level 1

A method is annotated `@Cacheable`. In proxy mode, another public method of the same bean calls it as `this.method()`. Does the advice of the annotation run for this call?

a) Yes: Spring Boot proxies all of its beans, so every call to any method is advised
b) No: a call on `this` bypasses the proxy, so the interceptor chain does not run it
c) Yes: the annotation is on that method, and its presence alone triggers the advice
d) Yes: `this` is the proxy inside the bean, so the call is intercepted all the same

**Key: b**

Explanation: Inputs: `@Cacheable`, call shape: self-invocation. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call runs on `this`, inside the target object, and never reaches the proxy. Step 2: the call bypassed the proxy, so the method's visibility does not matter. Result: No: a call on `this` bypasses the proxy, so the interceptor chain does not run it. The other options are misreadings: yes: the annotation is on that method, and its presence alone triggers the advice; yes: spring boot proxies all of its beans, so every call to any method is advised; yes: `this` is the proxy inside the bean, so the call is intercepted all the same. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 11. seed 3200880193863446211, level 1

A method is annotated `@Cacheable`. In proxy mode, another public method of the bean calls it through a self reference. Does the advice of the annotation run for this call?

a) No: a call from inside the bean always runs on `this` and never reaches the proxy
b) No: a bean cannot hold a reference to its own proxy, so the advice is always lost
c) Yes: the call goes through the injected proxy, not through `this`, so advice runs
d) No: the proxy advises a method only if the caller bean carries the annotation too

**Key: c**

Explanation: Inputs: `@Cacheable`, call shape: self-injection. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy held in the self reference. Step 2: the method is public, so the proxy can advise it. Result: Yes: the call goes through the injected proxy, not through `this`, so advice runs. The other options are misreadings: no: a call from inside the bean always runs on `this` and never reaches the proxy; no: a bean cannot hold a reference to its own proxy, so the advice is always lost; no: the proxy advises a method only if the caller bean carries the annotation too. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 12. seed 1499774523791030832, level 1

A method is annotated `@Transactional`. In proxy mode, another public method of the same bean calls it as `this.method()`. Does the advice of the annotation run for this call?

a) Yes: the annotation is on that method, and its presence alone triggers the advice
b) Yes: Spring Boot proxies all of its beans, so every call to any method is advised
c) No: a call on `this` bypasses the proxy, so the interceptor chain does not run it
d) Yes: `this` is the proxy inside the bean, so the call is intercepted all the same

**Key: c**

Explanation: Inputs: `@Transactional`, call shape: self-invocation. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call runs on `this`, inside the target object, and never reaches the proxy. Step 2: the call bypassed the proxy, so the method's visibility does not matter. Result: No: a call on `this` bypasses the proxy, so the interceptor chain does not run it. The other options are misreadings: yes: the annotation is on that method, and its presence alone triggers the advice; yes: spring boot proxies all of its beans, so every call to any method is advised; yes: `this` is the proxy inside the bean, so the call is intercepted all the same. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 13. seed 2350178718794314673, level 1

A method is annotated `@Cacheable`. In proxy mode, another public method of the bean calls it through a self reference. Does the advice of the annotation run for this call?

a) No: a call from inside the bean always runs on `this` and never reaches the proxy
b) No: a bean cannot hold a reference to its own proxy, so the advice is always lost
c) Yes: the call goes through the injected proxy, not through `this`, so advice runs
d) No: the proxy advises a method only if the caller bean carries the annotation too

**Key: c**

Explanation: Inputs: `@Cacheable`, call shape: self-injection. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy held in the self reference. Step 2: the method is public, so the proxy can advise it. Result: Yes: the call goes through the injected proxy, not through `this`, so advice runs. The other options are misreadings: no: a call from inside the bean always runs on `this` and never reaches the proxy; no: a bean cannot hold a reference to its own proxy, so the advice is always lost; no: the proxy advises a method only if the caller bean carries the annotation too. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 14. seed 1327778385700196157, level 2

A method is annotated `@Async`. In proxy mode, another public method of the same bean calls its `private` method. Does the advice of the annotation run for this call?

a) Yes: a class-based proxy can advise `private` methods, so the call is intercepted
b) Yes: Spring Boot proxies all of its beans, so every call to any method is advised
c) Yes: the annotation is on that method, and its presence alone triggers the advice
d) No: a `private` method cannot be overridden by a subclass, so no proxy advises it

**Key: d**

Explanation: Inputs: `@Async`, call shape: private. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call runs on `this`, inside the target object, and never reaches the proxy. Step 2: the method is `private`, so even a proxy could not advise it. Result: No: a `private` method cannot be overridden by a subclass, so no proxy advises it. The other options are misreadings: yes: the annotation is on that method, and its presence alone triggers the advice; yes: spring boot proxies all of its beans, so every call to any method is advised; yes: a class-based proxy can advise `private` methods, so the call is intercepted. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 15. seed 1501448108601260324, level 2

A method is annotated `@Transactional`. In AspectJ mode, another public method of the same bean calls it as `this.method()`. Does the advice of the annotation run for this call?

a) Yes: AspectJ weaving puts the advice in the bytecode, so no proxy is left to skip
b) No: AspectJ mode needs a proxy too, and a call on `this` always misses that proxy
c) No: a call on `this` bypasses the proxy, so the interceptor chain does not run it
d) No: AspectJ mode advises only calls arriving from another bean, never from `this`

**Key: a**

Explanation: Inputs: `@Transactional`, call shape: aspectj. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: there is no proxy: the advice is woven into the bytecode, so every call is advised. Step 2: woven advice does not depend on overriding the method. Result: Yes: AspectJ weaving puts the advice in the bytecode, so no proxy is left to skip. The other options are misreadings: no: a call on `this` bypasses the proxy, so the interceptor chain does not run it; no: aspectj mode needs a proxy too, and a call on `this` always misses that proxy; no: aspectj mode advises only calls arriving from another bean, never from `this`. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 16. seed 3415372749177803700, level 1

A method is annotated `@Async`. In proxy mode, another bean calls the public method through its injected reference. Does the advice of the annotation run for this call?

a) Yes: the call comes in through the proxy, which then runs its interceptors for it
b) No: the injected reference is the raw target object, and the call skips the proxy
c) No: advice runs only for calls made from inside the same bean, never from another
d) No: the proxy advises a method only when the calling bean also has the annotation

**Key: a**

Explanation: Inputs: `@Async`, call shape: external. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy. Step 2: the method is public, so the proxy can advise it. Result: Yes: the call comes in through the proxy, which then runs its interceptors for it. The other options are misreadings: no: the injected reference is the raw target object, and the call skips the proxy; no: the proxy advises a method only when the calling bean also has the annotation; no: advice runs only for calls made from inside the same bean, never from another. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 17. seed 884693505425421041, level 2

A method is annotated `@Cacheable`. In proxy mode, another public method of the same bean calls its `private` method. Does the advice of the annotation run for this call?

a) Yes: the annotation is on that method, and its presence alone triggers the advice
b) Yes: Spring Boot proxies all of its beans, so every call to any method is advised
c) No: a `private` method cannot be overridden by a subclass, so no proxy advises it
d) Yes: a class-based proxy can advise `private` methods, so the call is intercepted

**Key: c**

Explanation: Inputs: `@Cacheable`, call shape: private. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call runs on `this`, inside the target object, and never reaches the proxy. Step 2: the method is `private`, so even a proxy could not advise it. Result: No: a `private` method cannot be overridden by a subclass, so no proxy advises it. The other options are misreadings: yes: the annotation is on that method, and its presence alone triggers the advice; yes: spring boot proxies all of its beans, so every call to any method is advised; yes: a class-based proxy can advise `private` methods, so the call is intercepted. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 18. seed 4066362098620395868, level 1

A method is annotated `@Cacheable`. In proxy mode, another bean calls the public method through its injected reference. Does the advice of the annotation run for this call?

a) No: the proxy advises a method only when the calling bean also has the annotation
b) Yes: the call comes in through the proxy, which then runs its interceptors for it
c) No: the injected reference is the raw target object, and the call skips the proxy
d) No: advice runs only for calls made from inside the same bean, never from another

**Key: b**

Explanation: Inputs: `@Cacheable`, call shape: external. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy. Step 2: the method is public, so the proxy can advise it. Result: Yes: the call comes in through the proxy, which then runs its interceptors for it. The other options are misreadings: no: the injected reference is the raw target object, and the call skips the proxy; no: the proxy advises a method only when the calling bean also has the annotation; no: advice runs only for calls made from inside the same bean, never from another. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 19. seed 4395317076025824127, level 1

A method is annotated `@Cacheable`. In proxy mode, another bean calls the public method through its injected reference. Does the advice of the annotation run for this call?

a) No: advice runs only for calls made from inside the same bean, never from another
b) Yes: the call comes in through the proxy, which then runs its interceptors for it
c) No: the injected reference is the raw target object, and the call skips the proxy
d) No: the proxy advises a method only when the calling bean also has the annotation

**Key: b**

Explanation: Inputs: `@Cacheable`, call shape: external. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy. Step 2: the method is public, so the proxy can advise it. Result: Yes: the call comes in through the proxy, which then runs its interceptors for it. The other options are misreadings: no: the injected reference is the raw target object, and the call skips the proxy; no: the proxy advises a method only when the calling bean also has the annotation; no: advice runs only for calls made from inside the same bean, never from another. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 20. seed 2397806506097962750, level 1

A method is annotated `@Cacheable`. In proxy mode, another bean calls the public method through its injected reference. Does the advice of the annotation run for this call?

a) No: advice runs only for calls made from inside the same bean, never from another
b) Yes: the call comes in through the proxy, which then runs its interceptors for it
c) No: the injected reference is the raw target object, and the call skips the proxy
d) No: the proxy advises a method only when the calling bean also has the annotation

**Key: b**

Explanation: Inputs: `@Cacheable`, call shape: external. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy. Step 2: the method is public, so the proxy can advise it. Result: Yes: the call comes in through the proxy, which then runs its interceptors for it. The other options are misreadings: no: the injected reference is the raw target object, and the call skips the proxy; no: the proxy advises a method only when the calling bean also has the annotation; no: advice runs only for calls made from inside the same bean, never from another. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 21. seed 2849241914364087844, level 2

A method is annotated `@Async`. In proxy mode, the class has no interface and another bean calls its public `final` method. Does the advice of the annotation run for this call?

a) Yes: Spring Boot proxies all of its beans, so every call to any method is advised
b) No: a class-based proxy extends the class and so cannot override a `final` method
c) Yes: the annotation is on that method, and its presence alone triggers the advice
d) Yes: the call comes in through the proxy, hence the interceptor chain runs for it

**Key: b**

Explanation: Inputs: `@Async`, call shape: final. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy. Step 2: the method is `final`, so a class-based proxy cannot override or advise it. Result: No: a class-based proxy extends the class and so cannot override a `final` method. The other options are misreadings: yes: the annotation is on that method, and its presence alone triggers the advice; yes: spring boot proxies all of its beans, so every call to any method is advised; yes: the call comes in through the proxy, hence the interceptor chain runs for it. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 22. seed 4600447579687542479, level 2

A method is annotated `@Cacheable`. In proxy mode, another public method of the same bean calls it as `this.method()`. Does the advice of the annotation run for this call?

a) No: a call on `this` bypasses the proxy, so the interceptor chain does not run it
b) Yes: Spring Boot proxies all of its beans, so every call to any method is advised
c) Yes: `this` is the proxy inside the bean, so the call is intercepted all the same
d) Yes: the annotation is on that method, and its presence alone triggers the advice

**Key: a**

Explanation: Inputs: `@Cacheable`, call shape: self-invocation. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call runs on `this`, inside the target object, and never reaches the proxy. Step 2: the call bypassed the proxy, so the method's visibility does not matter. Result: No: a call on `this` bypasses the proxy, so the interceptor chain does not run it. The other options are misreadings: yes: the annotation is on that method, and its presence alone triggers the advice; yes: spring boot proxies all of its beans, so every call to any method is advised; yes: `this` is the proxy inside the bean, so the call is intercepted all the same. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 23. seed 989673874183161540, level 1

A method is annotated `@Cacheable`. In proxy mode, another bean calls the public method through its injected reference. Does the advice of the annotation run for this call?

a) No: advice runs only for calls made from inside the same bean, never from another
b) Yes: the call comes in through the proxy, which then runs its interceptors for it
c) No: the proxy advises a method only when the calling bean also has the annotation
d) No: the injected reference is the raw target object, and the call skips the proxy

**Key: b**

Explanation: Inputs: `@Cacheable`, call shape: external. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy. Step 2: the method is public, so the proxy can advise it. Result: Yes: the call comes in through the proxy, which then runs its interceptors for it. The other options are misreadings: no: the injected reference is the raw target object, and the call skips the proxy; no: the proxy advises a method only when the calling bean also has the annotation; no: advice runs only for calls made from inside the same bean, never from another. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 24. seed 3693091364344815618, level 1

A method is annotated `@Async`. In proxy mode, another public method of the same bean calls it as `this.method()`. Does the advice of the annotation run for this call?

a) No: a call on `this` bypasses the proxy, so the interceptor chain does not run it
b) Yes: `this` is the proxy inside the bean, so the call is intercepted all the same
c) Yes: Spring Boot proxies all of its beans, so every call to any method is advised
d) Yes: the annotation is on that method, and its presence alone triggers the advice

**Key: a**

Explanation: Inputs: `@Async`, call shape: self-invocation. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call runs on `this`, inside the target object, and never reaches the proxy. Step 2: the call bypassed the proxy, so the method's visibility does not matter. Result: No: a call on `this` bypasses the proxy, so the interceptor chain does not run it. The other options are misreadings: yes: the annotation is on that method, and its presence alone triggers the advice; yes: spring boot proxies all of its beans, so every call to any method is advised; yes: `this` is the proxy inside the bean, so the call is intercepted all the same. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 25. seed 818159185674710258, level 2

A method is annotated `@Async`. In proxy mode, another public method of the same bean calls it as `this.method()`. Does the advice of the annotation run for this call?

a) Yes: the annotation is on that method, and its presence alone triggers the advice
b) Yes: Spring Boot proxies all of its beans, so every call to any method is advised
c) Yes: `this` is the proxy inside the bean, so the call is intercepted all the same
d) No: a call on `this` bypasses the proxy, so the interceptor chain does not run it

**Key: d**

Explanation: Inputs: `@Async`, call shape: self-invocation. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call runs on `this`, inside the target object, and never reaches the proxy. Step 2: the call bypassed the proxy, so the method's visibility does not matter. Result: No: a call on `this` bypasses the proxy, so the interceptor chain does not run it. The other options are misreadings: yes: the annotation is on that method, and its presence alone triggers the advice; yes: spring boot proxies all of its beans, so every call to any method is advised; yes: `this` is the proxy inside the bean, so the call is intercepted all the same. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 26. seed 2353295002485243694, level 1

A method is annotated `@Cacheable`. In proxy mode, another public method of the same bean calls it as `this.method()`. Does the advice of the annotation run for this call?

a) No: a call on `this` bypasses the proxy, so the interceptor chain does not run it
b) Yes: `this` is the proxy inside the bean, so the call is intercepted all the same
c) Yes: the annotation is on that method, and its presence alone triggers the advice
d) Yes: Spring Boot proxies all of its beans, so every call to any method is advised

**Key: a**

Explanation: Inputs: `@Cacheable`, call shape: self-invocation. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call runs on `this`, inside the target object, and never reaches the proxy. Step 2: the call bypassed the proxy, so the method's visibility does not matter. Result: No: a call on `this` bypasses the proxy, so the interceptor chain does not run it. The other options are misreadings: yes: the annotation is on that method, and its presence alone triggers the advice; yes: spring boot proxies all of its beans, so every call to any method is advised; yes: `this` is the proxy inside the bean, so the call is intercepted all the same. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 27. seed 1725216171887405897, level 1

A method is annotated `@Cacheable`. In proxy mode, another public method of the same bean calls it as `this.method()`. Does the advice of the annotation run for this call?

a) Yes: `this` is the proxy inside the bean, so the call is intercepted all the same
b) Yes: the annotation is on that method, and its presence alone triggers the advice
c) Yes: Spring Boot proxies all of its beans, so every call to any method is advised
d) No: a call on `this` bypasses the proxy, so the interceptor chain does not run it

**Key: d**

Explanation: Inputs: `@Cacheable`, call shape: self-invocation. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call runs on `this`, inside the target object, and never reaches the proxy. Step 2: the call bypassed the proxy, so the method's visibility does not matter. Result: No: a call on `this` bypasses the proxy, so the interceptor chain does not run it. The other options are misreadings: yes: the annotation is on that method, and its presence alone triggers the advice; yes: spring boot proxies all of its beans, so every call to any method is advised; yes: `this` is the proxy inside the bean, so the call is intercepted all the same. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 28. seed 494358562355162095, level 2

A method is annotated `@Cacheable`. In proxy mode, another bean calls the public method through its injected reference. Does the advice of the annotation run for this call?

a) No: advice runs only for calls made from inside the same bean, never from another
b) No: the proxy advises a method only when the calling bean also has the annotation
c) No: the injected reference is the raw target object, and the call skips the proxy
d) Yes: the call comes in through the proxy, which then runs its interceptors for it

**Key: d**

Explanation: Inputs: `@Cacheable`, call shape: external. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy. Step 2: the method is public, so the proxy can advise it. Result: Yes: the call comes in through the proxy, which then runs its interceptors for it. The other options are misreadings: no: the injected reference is the raw target object, and the call skips the proxy; no: the proxy advises a method only when the calling bean also has the annotation; no: advice runs only for calls made from inside the same bean, never from another. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 29. seed 1643241378344290083, level 2

A method is annotated `@Transactional`. In proxy mode, another public method of the same bean calls it as `this.method()`. Does the advice of the annotation run for this call?

a) No: a call on `this` bypasses the proxy, so the interceptor chain does not run it
b) Yes: Spring Boot proxies all of its beans, so every call to any method is advised
c) Yes: `this` is the proxy inside the bean, so the call is intercepted all the same
d) Yes: the annotation is on that method, and its presence alone triggers the advice

**Key: a**

Explanation: Inputs: `@Transactional`, call shape: self-invocation. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call runs on `this`, inside the target object, and never reaches the proxy. Step 2: the call bypassed the proxy, so the method's visibility does not matter. Result: No: a call on `this` bypasses the proxy, so the interceptor chain does not run it. The other options are misreadings: yes: the annotation is on that method, and its presence alone triggers the advice; yes: spring boot proxies all of its beans, so every call to any method is advised; yes: `this` is the proxy inside the bean, so the call is intercepted all the same. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 30. seed 247835090375470289, level 2

A method is annotated `@Cacheable`. In proxy mode, another public method of the same bean calls it as `this.method()`. Does the advice of the annotation run for this call?

a) Yes: the annotation is on that method, and its presence alone triggers the advice
b) Yes: `this` is the proxy inside the bean, so the call is intercepted all the same
c) No: a call on `this` bypasses the proxy, so the interceptor chain does not run it
d) Yes: Spring Boot proxies all of its beans, so every call to any method is advised

**Key: c**

Explanation: Inputs: `@Cacheable`, call shape: self-invocation. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call runs on `this`, inside the target object, and never reaches the proxy. Step 2: the call bypassed the proxy, so the method's visibility does not matter. Result: No: a call on `this` bypasses the proxy, so the interceptor chain does not run it. The other options are misreadings: yes: the annotation is on that method, and its presence alone triggers the advice; yes: spring boot proxies all of its beans, so every call to any method is advised; yes: `this` is the proxy inside the bean, so the call is intercepted all the same. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 31. seed 1107026886128396375, level 1

A method is annotated `@Async`. In proxy mode, another public method of the same bean calls it as `this.method()`. Does the advice of the annotation run for this call?

a) Yes: Spring Boot proxies all of its beans, so every call to any method is advised
b) No: a call on `this` bypasses the proxy, so the interceptor chain does not run it
c) Yes: the annotation is on that method, and its presence alone triggers the advice
d) Yes: `this` is the proxy inside the bean, so the call is intercepted all the same

**Key: b**

Explanation: Inputs: `@Async`, call shape: self-invocation. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call runs on `this`, inside the target object, and never reaches the proxy. Step 2: the call bypassed the proxy, so the method's visibility does not matter. Result: No: a call on `this` bypasses the proxy, so the interceptor chain does not run it. The other options are misreadings: yes: the annotation is on that method, and its presence alone triggers the advice; yes: spring boot proxies all of its beans, so every call to any method is advised; yes: `this` is the proxy inside the bean, so the call is intercepted all the same. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 32. seed 2442669350174419619, level 2

A method is annotated `@Transactional`. In AspectJ mode, another public method of the same bean calls it as `this.method()`. Does the advice of the annotation run for this call?

a) No: a call on `this` bypasses the proxy, so the interceptor chain does not run it
b) Yes: AspectJ weaving puts the advice in the bytecode, so no proxy is left to skip
c) No: AspectJ mode needs a proxy too, and a call on `this` always misses that proxy
d) No: AspectJ mode advises only calls arriving from another bean, never from `this`

**Key: b**

Explanation: Inputs: `@Transactional`, call shape: aspectj. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: there is no proxy: the advice is woven into the bytecode, so every call is advised. Step 2: woven advice does not depend on overriding the method. Result: Yes: AspectJ weaving puts the advice in the bytecode, so no proxy is left to skip. The other options are misreadings: no: a call on `this` bypasses the proxy, so the interceptor chain does not run it; no: aspectj mode needs a proxy too, and a call on `this` always misses that proxy; no: aspectj mode advises only calls arriving from another bean, never from `this`. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 33. seed 2811967552906907475, level 1

A method is annotated `@Async`. In proxy mode, another public method of the bean calls it through a self reference. Does the advice of the annotation run for this call?

a) Yes: the call goes through the injected proxy, not through `this`, so advice runs
b) No: the proxy advises a method only if the caller bean carries the annotation too
c) No: a call from inside the bean always runs on `this` and never reaches the proxy
d) No: a bean cannot hold a reference to its own proxy, so the advice is always lost

**Key: a**

Explanation: Inputs: `@Async`, call shape: self-injection. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy held in the self reference. Step 2: the method is public, so the proxy can advise it. Result: Yes: the call goes through the injected proxy, not through `this`, so advice runs. The other options are misreadings: no: a call from inside the bean always runs on `this` and never reaches the proxy; no: a bean cannot hold a reference to its own proxy, so the advice is always lost; no: the proxy advises a method only if the caller bean carries the annotation too. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 34. seed 379310593878976199, level 1

A method is annotated `@Async`. In proxy mode, another public method of the bean calls it through a self reference. Does the advice of the annotation run for this call?

a) Yes: the call goes through the injected proxy, not through `this`, so advice runs
b) No: a bean cannot hold a reference to its own proxy, so the advice is always lost
c) No: the proxy advises a method only if the caller bean carries the annotation too
d) No: a call from inside the bean always runs on `this` and never reaches the proxy

**Key: a**

Explanation: Inputs: `@Async`, call shape: self-injection. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy held in the self reference. Step 2: the method is public, so the proxy can advise it. Result: Yes: the call goes through the injected proxy, not through `this`, so advice runs. The other options are misreadings: no: a call from inside the bean always runs on `this` and never reaches the proxy; no: a bean cannot hold a reference to its own proxy, so the advice is always lost; no: the proxy advises a method only if the caller bean carries the annotation too. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 35. seed 1181362306026767059, level 2

A method is annotated `@Transactional`. In AspectJ mode, another public method of the same bean calls it as `this.method()`. Does the advice of the annotation run for this call?

a) Yes: AspectJ weaving puts the advice in the bytecode, so no proxy is left to skip
b) No: AspectJ mode advises only calls arriving from another bean, never from `this`
c) No: AspectJ mode needs a proxy too, and a call on `this` always misses that proxy
d) No: a call on `this` bypasses the proxy, so the interceptor chain does not run it

**Key: a**

Explanation: Inputs: `@Transactional`, call shape: aspectj. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: there is no proxy: the advice is woven into the bytecode, so every call is advised. Step 2: woven advice does not depend on overriding the method. Result: Yes: AspectJ weaving puts the advice in the bytecode, so no proxy is left to skip. The other options are misreadings: no: a call on `this` bypasses the proxy, so the interceptor chain does not run it; no: aspectj mode needs a proxy too, and a call on `this` always misses that proxy; no: aspectj mode advises only calls arriving from another bean, never from `this`. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 36. seed 1236500378347204874, level 2

A method is annotated `@Transactional`. In proxy mode, another public method of the same bean calls it as `this.method()`. Does the advice of the annotation run for this call?

a) Yes: `this` is the proxy inside the bean, so the call is intercepted all the same
b) No: a call on `this` bypasses the proxy, so the interceptor chain does not run it
c) Yes: the annotation is on that method, and its presence alone triggers the advice
d) Yes: Spring Boot proxies all of its beans, so every call to any method is advised

**Key: b**

Explanation: Inputs: `@Transactional`, call shape: self-invocation. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call runs on `this`, inside the target object, and never reaches the proxy. Step 2: the call bypassed the proxy, so the method's visibility does not matter. Result: No: a call on `this` bypasses the proxy, so the interceptor chain does not run it. The other options are misreadings: yes: the annotation is on that method, and its presence alone triggers the advice; yes: spring boot proxies all of its beans, so every call to any method is advised; yes: `this` is the proxy inside the bean, so the call is intercepted all the same. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 37. seed 1024350431535688015, level 1

A method is annotated `@Cacheable`. In proxy mode, another public method of the bean calls it through a self reference. Does the advice of the annotation run for this call?

a) No: a bean cannot hold a reference to its own proxy, so the advice is always lost
b) No: a call from inside the bean always runs on `this` and never reaches the proxy
c) Yes: the call goes through the injected proxy, not through `this`, so advice runs
d) No: the proxy advises a method only if the caller bean carries the annotation too

**Key: c**

Explanation: Inputs: `@Cacheable`, call shape: self-injection. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy held in the self reference. Step 2: the method is public, so the proxy can advise it. Result: Yes: the call goes through the injected proxy, not through `this`, so advice runs. The other options are misreadings: no: a call from inside the bean always runs on `this` and never reaches the proxy; no: a bean cannot hold a reference to its own proxy, so the advice is always lost; no: the proxy advises a method only if the caller bean carries the annotation too. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 38. seed 3645318346409052748, level 1

A method is annotated `@Transactional`. In proxy mode, another public method of the same bean calls it as `this.method()`. Does the advice of the annotation run for this call?

a) Yes: Spring Boot proxies all of its beans, so every call to any method is advised
b) No: a call on `this` bypasses the proxy, so the interceptor chain does not run it
c) Yes: the annotation is on that method, and its presence alone triggers the advice
d) Yes: `this` is the proxy inside the bean, so the call is intercepted all the same

**Key: b**

Explanation: Inputs: `@Transactional`, call shape: self-invocation. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call runs on `this`, inside the target object, and never reaches the proxy. Step 2: the call bypassed the proxy, so the method's visibility does not matter. Result: No: a call on `this` bypasses the proxy, so the interceptor chain does not run it. The other options are misreadings: yes: the annotation is on that method, and its presence alone triggers the advice; yes: spring boot proxies all of its beans, so every call to any method is advised; yes: `this` is the proxy inside the bean, so the call is intercepted all the same. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 39. seed 2174487737402384867, level 1

A method is annotated `@Transactional`. In proxy mode, another bean calls the public method through its injected reference. Does the advice of the annotation run for this call?

a) No: advice runs only for calls made from inside the same bean, never from another
b) Yes: the call comes in through the proxy, which then runs its interceptors for it
c) No: the proxy advises a method only when the calling bean also has the annotation
d) No: the injected reference is the raw target object, and the call skips the proxy

**Key: b**

Explanation: Inputs: `@Transactional`, call shape: external. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy. Step 2: the method is public, so the proxy can advise it. Result: Yes: the call comes in through the proxy, which then runs its interceptors for it. The other options are misreadings: no: the injected reference is the raw target object, and the call skips the proxy; no: the proxy advises a method only when the calling bean also has the annotation; no: advice runs only for calls made from inside the same bean, never from another. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 40. seed 4298243331845847083, level 1

A method is annotated `@Transactional`. In proxy mode, another public method of the bean calls it through a self reference. Does the advice of the annotation run for this call?

a) No: the proxy advises a method only if the caller bean carries the annotation too
b) No: a call from inside the bean always runs on `this` and never reaches the proxy
c) No: a bean cannot hold a reference to its own proxy, so the advice is always lost
d) Yes: the call goes through the injected proxy, not through `this`, so advice runs

**Key: d**

Explanation: Inputs: `@Transactional`, call shape: self-injection. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy held in the self reference. Step 2: the method is public, so the proxy can advise it. Result: Yes: the call goes through the injected proxy, not through `this`, so advice runs. The other options are misreadings: no: a call from inside the bean always runs on `this` and never reaches the proxy; no: a bean cannot hold a reference to its own proxy, so the advice is always lost; no: the proxy advises a method only if the caller bean carries the annotation too. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 41. seed 796590298615414427, level 1

A method is annotated `@Transactional`. In proxy mode, another public method of the bean calls it through a self reference. Does the advice of the annotation run for this call?

a) No: a call from inside the bean always runs on `this` and never reaches the proxy
b) No: a bean cannot hold a reference to its own proxy, so the advice is always lost
c) Yes: the call goes through the injected proxy, not through `this`, so advice runs
d) No: the proxy advises a method only if the caller bean carries the annotation too

**Key: c**

Explanation: Inputs: `@Transactional`, call shape: self-injection. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy held in the self reference. Step 2: the method is public, so the proxy can advise it. Result: Yes: the call goes through the injected proxy, not through `this`, so advice runs. The other options are misreadings: no: a call from inside the bean always runs on `this` and never reaches the proxy; no: a bean cannot hold a reference to its own proxy, so the advice is always lost; no: the proxy advises a method only if the caller bean carries the annotation too. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 42. seed 3334232281307558444, level 1

A method is annotated `@Transactional`. In proxy mode, another bean calls the public method through its injected reference. Does the advice of the annotation run for this call?

a) No: advice runs only for calls made from inside the same bean, never from another
b) Yes: the call comes in through the proxy, which then runs its interceptors for it
c) No: the injected reference is the raw target object, and the call skips the proxy
d) No: the proxy advises a method only when the calling bean also has the annotation

**Key: b**

Explanation: Inputs: `@Transactional`, call shape: external. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy. Step 2: the method is public, so the proxy can advise it. Result: Yes: the call comes in through the proxy, which then runs its interceptors for it. The other options are misreadings: no: the injected reference is the raw target object, and the call skips the proxy; no: the proxy advises a method only when the calling bean also has the annotation; no: advice runs only for calls made from inside the same bean, never from another. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 43. seed 1940888295425127857, level 2

A method is annotated `@Cacheable`. In proxy mode, another public method of the same bean calls its `private` method. Does the advice of the annotation run for this call?

a) No: a `private` method cannot be overridden by a subclass, so no proxy advises it
b) Yes: the annotation is on that method, and its presence alone triggers the advice
c) Yes: Spring Boot proxies all of its beans, so every call to any method is advised
d) Yes: a class-based proxy can advise `private` methods, so the call is intercepted

**Key: a**

Explanation: Inputs: `@Cacheable`, call shape: private. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call runs on `this`, inside the target object, and never reaches the proxy. Step 2: the method is `private`, so even a proxy could not advise it. Result: No: a `private` method cannot be overridden by a subclass, so no proxy advises it. The other options are misreadings: yes: the annotation is on that method, and its presence alone triggers the advice; yes: spring boot proxies all of its beans, so every call to any method is advised; yes: a class-based proxy can advise `private` methods, so the call is intercepted. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 44. seed 4307906744868066422, level 1

A method is annotated `@Async`. In proxy mode, another bean calls the public method through its injected reference. Does the advice of the annotation run for this call?

a) No: advice runs only for calls made from inside the same bean, never from another
b) No: the injected reference is the raw target object, and the call skips the proxy
c) Yes: the call comes in through the proxy, which then runs its interceptors for it
d) No: the proxy advises a method only when the calling bean also has the annotation

**Key: c**

Explanation: Inputs: `@Async`, call shape: external. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy. Step 2: the method is public, so the proxy can advise it. Result: Yes: the call comes in through the proxy, which then runs its interceptors for it. The other options are misreadings: no: the injected reference is the raw target object, and the call skips the proxy; no: the proxy advises a method only when the calling bean also has the annotation; no: advice runs only for calls made from inside the same bean, never from another. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 45. seed 2947548274128383785, level 2

A method is annotated `@Transactional`. In Spring Framework 7, with a class-based proxy, another bean calls a package-visible method. Does the advice of the annotation run for this call?

a) No: advice applies only to `public` methods, whatever the type of proxy is in use
b) Yes: a class-based proxy advises package-visible methods since Spring Framework 6
c) No: a class-based proxy can never override a package-visible method of its target
d) No: only methods declared on an interface are advised, whatever the visibility is

**Key: b**

Explanation: Inputs: `@Transactional`, call shape: package-private. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy. Step 2: the method is package-visible, which a class-based proxy can advise since 6.0. Result: Yes: a class-based proxy advises package-visible methods since Spring Framework 6. The other options are misreadings: no: advice applies only to `public` methods, whatever the type of proxy is in use; no: a class-based proxy can never override a package-visible method of its target; no: only methods declared on an interface are advised, whatever the visibility is. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 46. seed 625825868440630089, level 2

A method is annotated `@Async`. In proxy mode, another bean calls the public method through its injected reference. Does the advice of the annotation run for this call?

a) No: the injected reference is the raw target object, and the call skips the proxy
b) No: the proxy advises a method only when the calling bean also has the annotation
c) Yes: the call comes in through the proxy, which then runs its interceptors for it
d) No: advice runs only for calls made from inside the same bean, never from another

**Key: c**

Explanation: Inputs: `@Async`, call shape: external. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy. Step 2: the method is public, so the proxy can advise it. Result: Yes: the call comes in through the proxy, which then runs its interceptors for it. The other options are misreadings: no: the injected reference is the raw target object, and the call skips the proxy; no: the proxy advises a method only when the calling bean also has the annotation; no: advice runs only for calls made from inside the same bean, never from another. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 47. seed 1598838071060009303, level 2

A method is annotated `@Async`. In proxy mode, another public method of the same bean calls its `private` method. Does the advice of the annotation run for this call?

a) Yes: a class-based proxy can advise `private` methods, so the call is intercepted
b) Yes: the annotation is on that method, and its presence alone triggers the advice
c) No: a `private` method cannot be overridden by a subclass, so no proxy advises it
d) Yes: Spring Boot proxies all of its beans, so every call to any method is advised

**Key: c**

Explanation: Inputs: `@Async`, call shape: private. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call runs on `this`, inside the target object, and never reaches the proxy. Step 2: the method is `private`, so even a proxy could not advise it. Result: No: a `private` method cannot be overridden by a subclass, so no proxy advises it. The other options are misreadings: yes: the annotation is on that method, and its presence alone triggers the advice; yes: spring boot proxies all of its beans, so every call to any method is advised; yes: a class-based proxy can advise `private` methods, so the call is intercepted. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 48. seed 285926011954418004, level 1

A method is annotated `@Async`. In proxy mode, another bean calls the public method through its injected reference. Does the advice of the annotation run for this call?

a) Yes: the call comes in through the proxy, which then runs its interceptors for it
b) No: advice runs only for calls made from inside the same bean, never from another
c) No: the proxy advises a method only when the calling bean also has the annotation
d) No: the injected reference is the raw target object, and the call skips the proxy

**Key: a**

Explanation: Inputs: `@Async`, call shape: external. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy. Step 2: the method is public, so the proxy can advise it. Result: Yes: the call comes in through the proxy, which then runs its interceptors for it. The other options are misreadings: no: the injected reference is the raw target object, and the call skips the proxy; no: the proxy advises a method only when the calling bean also has the annotation; no: advice runs only for calls made from inside the same bean, never from another. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 49. seed 342157712099284222, level 2

A method is annotated `@Transactional`. In Spring Framework 7, with a class-based proxy, another bean calls a package-visible method. Does the advice of the annotation run for this call?

a) No: advice applies only to `public` methods, whatever the type of proxy is in use
b) Yes: a class-based proxy advises package-visible methods since Spring Framework 6
c) No: only methods declared on an interface are advised, whatever the visibility is
d) No: a class-based proxy can never override a package-visible method of its target

**Key: b**

Explanation: Inputs: `@Transactional`, call shape: package-private. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy. Step 2: the method is package-visible, which a class-based proxy can advise since 6.0. Result: Yes: a class-based proxy advises package-visible methods since Spring Framework 6. The other options are misreadings: no: advice applies only to `public` methods, whatever the type of proxy is in use; no: a class-based proxy can never override a package-visible method of its target; no: only methods declared on an interface are advised, whatever the visibility is. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.

## 50. seed 980663959007157207, level 1

A method is annotated `@Transactional`. In proxy mode, another public method of the bean calls it through a self reference. Does the advice of the annotation run for this call?

a) No: a bean cannot hold a reference to its own proxy, so the advice is always lost
b) No: the proxy advises a method only if the caller bean carries the annotation too
c) No: a call from inside the bean always runs on `this` and never reaches the proxy
d) Yes: the call goes through the injected proxy, not through `this`, so advice runs

**Key: d**

Explanation: Inputs: `@Transactional`, call shape: self-injection. Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy can advise only the methods it is able to override; the mere presence of the annotation is not enough. Step 1: the call arrives through the proxy held in the self reference. Step 2: the method is public, so the proxy can advise it. Result: Yes: the call goes through the injected proxy, not through `this`, so advice runs. The other options are misreadings: no: a call from inside the bean always runs on `this` and never reaches the proxy; no: a bean cannot hold a reference to its own proxy, so the advice is always lost; no: the proxy advises a method only if the caller bean carries the annotation too. Source: `spring-fw-tx-declarative-annotations#using-transactional`; `spring-fw-aop-proxying#aop-understanding-aop-proxies`; `spring-fw-aop-proxying#proxying-mechanisms`.
