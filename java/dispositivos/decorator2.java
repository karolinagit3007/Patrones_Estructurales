package dispositivos;

interface Notificador {
    void enviar(String mensaje);
}

class NotificadorEmail implements Notificador {
    @Override
    public void enviar(String mensaje) {
        System.out.println("📧 Enviando Email: " + mensaje);
    }
}

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

class NotificadorSMS extends NotificadorDecorator {
    public NotificadorSMS(Notificador notificador) {
        super(notificador);
    }

    @Override
    public void enviar(String mensaje) {
        super.enviar(mensaje);  
        System.out.println("📩 Enviando SMS: " + mensaje);
    }
}

class NotificadorApp extends NotificadorDecorator {
    public NotificadorApp(Notificador notificador) {
        super(notificador);
    }

    @Override
    public void enviar(String mensaje) {
        super.enviar(mensaje);  
        System.out.println("📱 Enviando notificación en la App: " + mensaje);
    }
}

public class decorator2 {
    public static void main(String[] args) {
        Notificador notificadorBasico = new NotificadorEmail();

        Notificador notificadorSMS = new NotificadorSMS(notificadorBasico);

        Notificador notificadorCompleto = new NotificadorApp(notificadorSMS);

        System.out.println("🔔 Notificación enviada por una transacción bancaria:");
        notificadorCompleto.enviar("⚠️ Se ha realizado un retiro de $500 de su cuenta.");
    }
}


