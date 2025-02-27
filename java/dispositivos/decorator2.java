package dispositivos;

// Interfaz base de notificación
interface Notificador {
    void enviar(String mensaje);
}

// Implementación base: Notificación por Email
class NotificadorEmail implements Notificador {
    @Override
    public void enviar(String mensaje) {
        System.out.println("📧 Enviando Email: " + mensaje);
    }
}

// Decorador base
class NotificadorDecorator implements Notificador {
    protected Notificador notificador;

    public NotificadorDecorator(Notificador notificador) {
        this.notificador = notificador;
    }

    @Override
    public void enviar(String mensaje) {
        notificador.enviar(mensaje);
    }
}

// Decorador adicional: Notificación por SMS
class NotificadorSMS extends NotificadorDecorator {
    public NotificadorSMS(Notificador notificador) {
        super(notificador);
    }

    @Override
    public void enviar(String mensaje) {
        super.enviar(mensaje);  // Llama al método enviar del decorado (Email)
        System.out.println("📩 Enviando SMS: " + mensaje);
    }
}

// Decorador adicional: Notificación en App
class NotificadorApp extends NotificadorDecorator {
    public NotificadorApp(Notificador notificador) {
        super(notificador);
    }

    @Override
    public void enviar(String mensaje) {
        super.enviar(mensaje);  // Llama al método enviar del decorado (Email o SMS)
        System.out.println("📱 Enviando notificación en la App: " + mensaje);
    }
}

// Simulación de notificación por una transacción bancaria
public class decorator2 {
    public static void main(String[] args) {
        // Notificador básico solo con Email
        Notificador notificadorBasico = new NotificadorEmail();

        // Notificador con Email y SMS
        Notificador notificadorSMS = new NotificadorSMS(notificadorBasico);

        // Notificador con Email, SMS y Notificación en la App
        Notificador notificadorCompleto = new NotificadorApp(notificadorSMS);

        System.out.println("🔔 Notificación enviada por una transacción bancaria:");
        notificadorCompleto.enviar("⚠️ Se ha realizado un retiro de $500 de su cuenta.");
    }
}


