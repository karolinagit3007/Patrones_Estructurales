package dispositivos;


class Luces {
    public void encender() {
        System.out.println("💡 Luces encendidas");
    }

    public void apagar() {
        System.out.println("💡 Luces apagadas");
    }
}

class AireAcondicionado {
    public void encender() {
        System.out.println("❄️ Aire acondicionado encendido");
    }

    public void apagar() {
        System.out.println("❄️ Aire acondicionado apagado");
    }
}

class Alarma {
    public void activar() {
        System.out.println("🚨 Alarma de emergencia activada");
    }

    public void desactivar() {
        System.out.println("🚨 Alarma desactivada");
    }
}

class HospitalInteligente {
    private Luces luces;
    private AireAcondicionado aire;
    private Alarma alarma;

    public HospitalInteligente() {
        luces = new Luces();
        aire = new AireAcondicionado();
        alarma = new Alarma();
    }

    public void modoEmergencia() {
        System.out.println("⚠️ Activando MODO EMERGENCIA...");
        luces.encender();
        aire.apagar();
        alarma.activar();
    }

    public void modoNormal() {
        System.out.println("✅ Activando MODO NORMAL...");
        luces.apagar();
        aire.encender();
        alarma.desactivar();
    }
}

public class facade2 {
    public static void main(String[] args) {
        HospitalInteligente hospital = new HospitalInteligente();

        hospital.modoNormal();
        hospital.modoEmergencia();
    }
}

