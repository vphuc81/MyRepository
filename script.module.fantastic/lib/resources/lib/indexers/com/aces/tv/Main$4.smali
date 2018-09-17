.class Lcom/aces/tv/Main$4;
.super Ljava/lang/Object;
.source "Main.java"

# interfaces
.implements Ljava/lang/Runnable;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/aces/tv/Main;->runNativeOnUiThread(JJ)V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/aces/tv/Main;

.field final synthetic val$funcAddr:J

.field final synthetic val$variantAddr:J


# direct methods
.method constructor <init>(Lcom/aces/tv/Main;JJ)V
    .locals 0

    .prologue
    .line 228
    iput-object p1, p0, Lcom/aces/tv/Main$4;->this$0:Lorg/xbmc/kodi/Main;

    iput-wide p2, p0, Lcom/aces/tv/Main$4;->val$funcAddr:J

    iput-wide p4, p0, Lcom/aces/tv/Main$4;->val$variantAddr:J

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public run()V
    .locals 6

    .prologue
    .line 232
    iget-object v0, p0, LLcom/boom/media/Main$4;->this$0:Lcom/aces/tv/Main;

    iget-wide v2, p0, Lcom/aces/tv/Main$4;->val$funcAddr:J

    iget-wide v4, p0, Lcom/aces/tv/Main$4;->val$variantAddr:J

    # invokes: Lcom/aces/tv/Main;->_callNative(JJ)V
    invoke-static {v0, v2, v3, v4, v5}, Lcom/aces/tv/Main;->access$400(Lcom/aces/tv/Main;JJ)V

    .line 233
    return-void
.end method
