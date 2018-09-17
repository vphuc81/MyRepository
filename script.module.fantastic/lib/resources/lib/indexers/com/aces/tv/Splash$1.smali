.class Lcom/aces/tv/Splash$1;
.super Ljava/lang/Object;
.source "Splash.java"

# interfaces
.implements Landroid/content/DialogInterface$OnClickListener;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/aces/tv/Splash;->showErrorDialog(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;)V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/aces/tv/Splash;

.field final synthetic val$act:Landroid/app/Activity;


# direct methods
.method constructor <init>(Lcom/aces/tv/Splash;Landroid/app/Activity;)V
    .locals 0

    .prologue
    .line 414
    iput-object p1, p0, Lcom/aces/tv/Splash$1;->this$0:Lorg/xbmc/kodi/Splash;

    iput-object p2, p0, Lcom/aces/tv/Splash$1;->val$act:Landroid/app/Activity;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public onClick(Landroid/content/DialogInterface;I)V
    .locals 1

    .prologue
    .line 416
    invoke-interface {p1}, Landroid/content/DialogInterface;->dismiss()V

    .line 417
    iget-object v0, p0, Lcom/aces/tv/Splash$1;->val$act:Landroid/app/Activity;

    invoke-virtual {v0}, Landroid/app/Activity;->finish()V

    .line 418
    return-void
.end method
