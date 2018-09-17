.class Lcom/aces/tv/Main$2;
.super Ljava/lang/Object;
.source "Main.java"

# interfaces
.implements Ljava/lang/Runnable;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/aces/tv/Main;->clearVideoView()V
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
    .line 73
    iput-object p1, p0, Lcom/aces/tv/Main$2;->this$0:Lorg/xbmc/kodi/Main;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public run()V
    .locals 1

    .prologue
    .line 77
    iget-object v0, p0, Lcom/aces/tv/Main$2;->this$0:Lorg/xbmc/kodi/Main;

    invoke-static {v0}, Lcom/aces/tv/Main;->access$000(Lorg/xbmc/kodi/Main;)Lorg/xbmc/kodi/XBMCVideoView;

    move-result-object v0

    invoke-virtual {v0}, Lorg/xbmc/kodi/XBMCVideoView;->clearSurface()V

    .line 78
    return-void
.end method
