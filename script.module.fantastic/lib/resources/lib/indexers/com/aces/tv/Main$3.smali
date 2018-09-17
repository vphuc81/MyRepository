.class Lcom/aces/tv/Main$3;
.super Ljava/lang/Object;
.source "Main.java"

# interfaces
.implements Landroid/view/View$OnSystemUiVisibilityChangeListener;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/aces/tv/Main;->onCreate(Landroid/os/Bundle;)V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/aces/tv/Main;


# direct methods
.method constructor <init>(Lcom/aces/tv/Main;)V
    .locals 0

    .prologue
    .line 127
    iput-object p1, p0, Lcom/aces/tv/Main$3;->this$0:Lcom/aces/tv/Main;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public onSystemUiVisibilityChange(I)V
    .locals 2

    .prologue
    .line 131
    and-int/lit8 v0, p1, 0x2

    if-nez v0, :cond_0

    .line 133
    iget-object v0, p0, Lcom/aces/tv/Main$3;->this$0:Lcom/aces/tv/Main;

    invoke-static {v0}, Lcom/aces/tv/Main;->access$300(Lorg/xbmc/kodi/Main;)Landroid/os/Handler;

    move-result-object v0

    new-instance v1, Lcom/aces/tv/Main$3$1;

    invoke-direct {v1, p0}, Lcom/aces/tv/Main$3$1;-><init>(Lorg/xbmc/kodi/Main$3;)V

    invoke-virtual {v0, v1}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z

    .line 154
    :cond_0
    return-void
.end method
